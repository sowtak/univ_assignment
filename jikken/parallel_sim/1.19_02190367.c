#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define rep(i, a, n)          \
  for (int i = a; i < n; i++) \
    ;
#define LX 1.0
#define LY 1.0
#define T 1.0
#define alpha 1.0
#define T_SPAN 20

void print_data(int MX, int MY, int n, double dx, double dy, double dt, double *u)
{
  FILE *fp;
  char sfile[256];
  int i, j;

  sprintf(sfile, "data_%06d.dat", n);
  fp = fopen(sfile, "w");
  fprintf(fp, "#time = %lf\n", (double)n * dt);
  fprintf(fp, "#x y u(x, y, t)\n");
  for (i = 0; i <= MX; i++)
  {
    for (j = 0; j <= MY; j++)
    {
      fprintf(fp, "%lf %lf %12lf\n", (double)i * dx, (double)j * dy, u[i * (MY + 1) + j]);
    }
    fprintf(fp, "\n");
  }
  fclose(fp);
  return;
}

int main(int argc, char *argv[])
{
  double *u, *uu, dx, dy, dt;
  int MX, MY, N, i, j, n;
  double S, SX, SY;

  MX = atoi(argv[1]);
  MY = atoi(argv[2]);
  N = atoi(argv[3]);
  S = 40000.0;
  SX = MX / 2;
  SY = MY / 2;
  dx = LX / MX;
  dy = LY / MY;
  dt = T / N;
  u = malloc(sizeof(double) * (MX + 1) * (MY + 1));
  uu = malloc(sizeof(double) * (MX + 1) * (MY + 1));

  for (i = 1; i < MX; i++)
  {
    for (j = 1; j < MY; j++)
    {
      u[i * (MY + 1) + j] = 0.0;
    }
  }
  for (i = 0; i <= MX; i++)
  {
    uu[i * (MY + 1)] = 0.0;
    uu[i * (MY + 1) + MY] = 0.0;
    u[i * (MY + 1)] = uu[i * (MY + 1)];
    u[i * (MY + 1) + MY] = uu[i * (MY + 1) + MY];
  }
  for (j = 0; j <= MY; j++)
  {
    uu[j] = 0.0;
    uu[MX * (MY + 1) + j] = 0.0;
    u[j] = uu[j];
    u[MX * (MY + 1) + j] = uu[MX * (MY + 1) + j];
  }

  printf("YES\n");
  print_data(MX, MY, 0, dx, dy, dt, u);

  for (n = 1; n <= N; n++)
  {
    for (i = 1; i < MX; i++)
    {
      for (j = 1; j < MY; j++)
      {
        if ((i == SX) && (j == SY))
        {
          uu[i * (MY + 1) + j] = dt * alpha * (((u[(i + 1) * (MY + 1) + j] - 2 * u[i * (MY + 1) + j] + u[(i - 1) * (MY + 1) + j]) / (dx * dx) + (u[i * (MY + 1) + (j + 1)] - 2 * u[i * (MY + 1) + j] + u[i * (MY + 1) + (j - 1)]) / (dy * dy))) + u[i * (MY + 1) + j] + (dt * S);
        }
        else
        {
          uu[i * (MY + 1) + j] = dt * alpha * (((u[(i + 1) * (MY + 1) + j] - 2 * u[i * (MY + 1) + j] + u[(i - 1) * (MY + 1) + j]) / (dx * dx) + (u[i * (MY + 1) + (j + 1)] - 2 * u[i * (MY + 1) + j] + u[i * (MY + 1) + (j - 1)]) / (dy * dy))) + u[i * (MY + 1) + j];
        }
      }
    }

    for (i = 1; i < MX; i++)
    {
      for (j = 1; j < MY; j++)
      {
        u[i * (MY + 1) + j] = uu[i * (MY + 1) + j];
      }
    }

    if (n % T_SPAN == 0)
      print_data(MX, MY, n, dx, dy, dt, u);
  }

  free(u);
  free(uu);

  return 0;
}
