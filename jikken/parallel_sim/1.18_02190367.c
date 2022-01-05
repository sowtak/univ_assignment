#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <mpi.h>

#define L 1.0
#define T 1.0
#define alpha 1.0
#define freq 1000

void print_data(int MX, int MY, int N, double dx, double dy, double dt, double *u[], int my_rank, int nprocs)
{

  FILE *fp;
  char sfile[256];
  int i, j;
  int start, end;
  int length;

  length = MX / nprocs;
  if (my_rank == 0)
  {
    start = 0;
    end = (my_rank + 1) * length;
  }
  else if (my_rank == nprocs - 1)
  {
    start = my_rank * length + 1;
    end = MX;
  }
  else
  {
    start = my_rank * length + 1;
    end = (my_rank + 1) * length;
  }

  if (nprocs == 1)
  {
    start = 0;
    end = MX;
  }

  sprintf(sfile, "dataMPI_%d_%06d.dat", my_rank, N);
  fp = fopen(sfile, "w");
  fprintf(fp, "#time = %lf\n", (double)N * dt);
  fprintf(fp, "#x y u(x, y, t)\n");
  for (i = start; i <= end; i++)
  {
    for (j = 0; j <= MY; j++)
    {
      fprintf(fp, "%lf %lf %12lf\n", (double)i * dx, (double)j * dy, u[i][j]);
    }
    fprintf(fp, "\n");
  }
  fclose(fp);
  return;
}

int main(int argc, char *argv[])
{
  int nprocs;
  int my_rank, prev_rank, next_rank;
  MPI_Status stat;
  struct timeval s;
  int length;
  double **u, **uu, dx, dy, dt;
  int MX, MY, N;
  int i, l_i, l_n, j, n;
  double t_start, t_end;
  int start, end;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  MX = 200;
  MY = 200;
  N = 160000;

  l_n = MX / nprocs;
  if (my_rank == nprocs - 1)
  {
    l_n += MX % nprocs;
  }

  u = (double **)malloc(sizeof(double *) * (l_n + 1));
  uu = (double **)malloc(sizeof(double *) * (l_n + 1));
  for (i = 0; i <= l_n; i++)
  {
    u[i] = (double *)malloc(sizeof(double) * (MY + 1));
    uu[i] = (double *)malloc(sizeof(double) * (MY + 1));
  }

  dx = L / MX;
  dy = L / MY;
  dt = T / N;

  if (my_rank == 0)
  {
    prev_rank = MPI_PROC_NULL;
    next_rank = my_rank + 1;
  }
  else if (my_rank == nprocs - 1)
  {
    prev_rank = my_rank - 1;
    next_rank = MPI_PROC_NULL;
  }
  else
  {
    prev_rank = my_rank - 1;
    next_rank = my_rank + 1;
  }

  length = MX / nprocs;

  if (my_rank == nprocs - 1)
  {
    start = my_rank * length + 1;
    end = MX - 1;
  }
  else
  {
    start = my_rank * length + 1;
    end = (my_rank + 1) * length;
  }

  if (nprocs == 1)
  {
    prev_rank = MPI_PROC_NULL;
    next_rank = MPI_PROC_NULL;
    start = 1;
    end = MX - 1;
  }

  for (i = 1; i < l_n; i++)
  {
    for (j = 1; j < MY; j++)
    {
      u[i][j] = 0.0;
    }
  }

  for (i = 0; i <= l_n; i++)
  {
    l_i = i + start;
    u[i][0] = 20 * l_i * dx + 10;
    u[i][MY] = 40 * l_i * dx + 40;
  }

  for (i = 0; i <= MY; i++)
  {
    u[0][i] = 30 * i * i * dy * dy + 10;
    u[l_n][i] = 50 * i * i * dy * dy + 30;
  }

  // print_data(MX, MY, 0, dx, dy, dt, u, my_rank, nprocs);

  MPI_Barrier(MPI_COMM_WORLD);
  t_start = MPI_Wtime();

  for (n = 1; n <= N; n++)
  {
    for (i = 1; i <= l_n; i++)
    {
      for (j = 1; j < MY; j++)
      {
        uu[i][j] = alpha * dt * ((u[i + 1][j] - 2 * u[i][j] + u[i - 1][j]) / dx / dx + (u[i][j + 1] - 2 * u[i][j] + u[i][j - 1]) / dy / dy) + u[i][j];
      }
    }
    for (i = 1; i <= l_n; i++)
    {
      for (j = 1; j < MY; j++)
      {
        u[i][j] = uu[i][j];
      }
    }
    printf("%d %d\n", n, my_rank);

    MPI_Sendrecv(&u[end][1], MY - 1, MPI_DOUBLE, next_rank, 0, &u[start - 1][1], MY - 1, MPI_DOUBLE, prev_rank, 0, MPI_COMM_WORLD, &stat);
    MPI_Sendrecv(&u[start][1], MY - 1, MPI_DOUBLE, prev_rank, 0, &u[end + 1][1], MY - 1, MPI_DOUBLE, next_rank, 0, MPI_COMM_WORLD, &stat);
    if (n % freq == 0)
      print_data(MX, MY, n, dx, dy, dt, u, my_rank, nprocs);
  }

  MPI_Barrier(MPI_COMM_WORLD);
  t_end = MPI_Wtime();

  printf("%f\n", t_end - t_start);

  MPI_Finalize();

  for (i = 0; i <= l_n; i++)
  {
    free(u[i]);
    free(uu[i]);
  }

  free(u);
  free(uu);

  return 0;
}
