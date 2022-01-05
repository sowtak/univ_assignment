#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#define rep(i, a, n) for (int i = a; i < n; i++)
#define LX 1.0
#define LY 1.0
#define T 1.0
#define alpha 1.0
#define T_SPAN 20
#define SIZE 505

int i, j, n;

double get_time()
{
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return tv.tv_sec + (double)tv.tv_usec * 1e-6;
}

void print_data(int Mx, int My, int n, double dx, double dy, double dt, double u[][SIZE])
{
  FILE *fp;
  char sfile[256];

  sprintf(sfile, "data_%06d.dat", n);
  fp = fopen(sfile, "w");
  fprintf(fp, "#time = %lf\n", (double)n * dt);
  fprintf(fp, "#x y u(x, y, t)\n");
  for (i = 0; i <= Mx; i++)
  {
    for (j = 0; j <= My; j++)
    {
      fprintf(fp, "%f %f %12f\n", (double)i * dx, (double)j * dy, u[i][j]);
    }
    fprintf(fp, "\n");
  }
  fclose(fp);
  return;
}

int main(int argc, char *argv[])
{
  double u[SIZE][SIZE], uu[SIZE][SIZE], dx, dy, dt;
  int MX, MY, N;
  double mx = 0;
  double t0, t1;

  MX = atoi(argv[1]);
  MY = atoi(argv[2]);
  N = atoi(argv[3]);
  dx = LX / MX;
  dy = LY / MY;
  dt = T / N;

  for (i = 0; i <= MX; i++)
  {
    for (j = 0; j <= MY; j++)
    {
      u[i][j] = 0.0;
    }
  }

  for (i = 0; i <= MX; i++)
  {
    u[i][0] = 20 * dx * i + 10;
    u[i][MY] = 40 * dx * i + 40;
  }
  for (j = 0; j <= MY; j++)
  {
    u[0][j] = 30 * dy * dy * j * j + 10;
    u[MX][j] = 50 * dy * dy * j * j + 30;
  }

  print_data(MX, MY, 0, dx, dy, dt, u);

  t0 = get_time();
  for (n = 1; n <= N; n++)
  {
    for (i = 1; i < MX; i++)
    {
      for (j = 1; j < MY; j++)
      {
        uu[i][j] = u[i][j] + dt * alpha * ((u[i + 1][j] - 2 * u[i][j] + u[i - 1][j]) / (dx * dx) + (u[i][j + 1] - 2 * u[i][j] + u[i][j - 1]) / (dy * dy));
      }
    }
    for (i = 1; i < MX; i++)
    {
      for (j = 1; j < MY; j++)
      {
        u[i][j] = uu[i][j];
      }
    }

    if (n % T_SPAN == 0)
    {
      print_data(MX, MY, n, dx, dy, dt, u);
    }
  }

  t1 = get_time();

  printf("%f\n", t1 - t0);

  return 0;
}
