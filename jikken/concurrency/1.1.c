#include <stdio.h>
#define L 1.0
#define T 1.0
#define alpha 1.0
#define T_SPAN 20


int main(int argc, char *argv[]) {
  double *u, *uu, dx, dt;

}

void print_data(int Mx, int n, double dx, double dt, double *u) {
  FILE *fp;
  char sfile[256];
  int i;

  sprintf(sfile, "data_%06d.dat", n);
  fp = fopen(sfile, "w");
  fprintf(fp, "#time = $lf\n", (double)n * dt);
  fprintf(fp, "#x u\n");
  for(i=0;i<=MX;i++) {
    fprintf(fp, "%lf %12lf\n", (double)i*dx, u[i]);
  }
  fclose(fp);
  return;

}
