#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>

#define L 1.0
#define T 1.0
#define alpha 1.0
#define T_SPAN 20
i, n;

void print_data(int MX, int n, double dx, double dt, double *u)
{
    FILE *fp;
    char sfile[256];
    int i;

    sprintf(sfile, "data_%06d.dat", n);
    fp = fopen(sfile, "w");
    fprintf(fp, "#time = %lf\n", (double)n * dt);
    fprintf(fp, "#x u\n");
    for (i = 0; i <= MX; i++)
    {
        fprintf(fp, "%lf %12lf\n", (double)i * dx, u[i]);
    }
    fclose(fp);
}

int main(int argc, char *argv[])
{
    double *u, *uu, dx, dt;
    int MX, N;
    dx = L / MX;
    dt = T / N;

    MX = atoi(argv[1]);
    N = atoi(argv[2]);
    for (i = 0; i <= MX; i++)
    {
        u[i] = 0.0;
    }
    print_data(MX, n, dx, dt, &u);

    for (n = 1; n <= N; n++)
    {
        for (i = 1; i < MX; i++)
        {
            uu[i] = u[i] + dt * alpha * ((u[i + 1] - 2 * u[i] + u[i - 1]) / (dx * dx) + u[i]);
        }
        for (i = 1; i < MX; i++)
        {
            u[i] = uu[i];
        }
        if (n % T_SPAN == 0)
        {
            print_data(MX, n, dx, dt, &n);
        }
    }

    return 0;
}
