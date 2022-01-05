#include <stdio.h>
#define L 1.0
#define T 1.0
#define alpha 1.0
#define T_SPAN 20

int main(int argc, char *argv[])
{
  double *u, *uu, dx, dt;
  int i = 0;
  int MX, N;

  MX = argv[0], N = argv[1];

  int x[MX];

  for (int i = 0; i <= MX; i++)
  {
    x[i] =
  }
  print_data(MX, N, dx, dt, u);

  for (int n = 1; n <= N; n++)
  {
    for (i = 1; i < MX; i++)
    {
    }

    for (i = 1; i < MX; i++)
    {
    }

    if (n % T_SPAN == 0)
    {
    }
  }
}

void print_data(int MX, int n, double dx, double dt, double *u)
{
  FILE *fp;
  char sfile[256];
  int i;

  sprintf(sfile, "data_%06d.dat", n);
  fp = fopen(sfile, "w");
  fprintf(fp, "#time = $lf\n", (double)n * dt);
  fprintf(fp, "#x u\n");
  for (i = 0; i <= MX; i++)
  {
    fprintf(fp, "%lf %12lf\n", (double)i * dx, u[i]);
  }
  fclose(fp);
  return;
}
