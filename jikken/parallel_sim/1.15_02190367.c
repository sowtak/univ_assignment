#include <stdio.h>
#include <mpi.h>
#define N 10000
int main(int argc, char *argv[])
{
  int n_procs;
  int my_rank;
  double val[N];
  MPI_Status stat;
  int i, l_n, l_istart, l_iend;
  double sum, tmp_sum;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &n_procs);
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  for (i = 0; i < N; i++)
  {
    val[i] = (double)i;
  }

  l_n = N / n_procs;
  if (my_rank == n_procs - 1)
  {
    l_n += N % n_procs;
  }

  l_istart = (N / n_procs) * my_rank;
  l_iend = l_istart + l_n - 1;
  sum = 0.0;
  for (i = l_istart; i <= l_iend; i++)
  {
    sum += val[i];
  }

  if (my_rank != 0)
  {
    MPI_Send(&sum, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
  }
  else
  {
    for (i = 1; i <= n_procs - 1; i++)
    {
      MPI_Recv(&tmp_sum, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD, &stat);
      sum += tmp_sum;
    }
  }

  printf("my rank is %d, n_procs is %d, sum is %8lf\n", my_rank, n_procs, sum);
  if (my_rank == 0)
  {
    printf("sum is %8lf\n", sum);
  }

  MPI_Finalize();

  return 0;
}
