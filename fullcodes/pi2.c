#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
int main(int argc, char *argv[]) {
  if (argc!=2) {
    printf("Program requires one argument, ntrials\n");
    exit(1);
  }
  long ntrials=strtol(argv[1],NULL,10); 
  long inside=0;
  long i;
  clock_t begin, end;
  double x, y, pi, seconds;
  double rmax=(double)RAND_MAX*(double)RAND_MAX;
  srand(time(NULL));
  begin=clock();
  for (i=0; i<ntrials; i++) {
    x=rand();
    y=rand();
    /*printf("%f %f\n",x,y);*/
    if (x*x+y*y < rmax) {
      inside++;
    }
  }
  pi=4.*(double)inside/(double)ntrials;
  end=clock();
  seconds=(double)(end-begin)/CLOCKS_PER_SEC;
  printf("pi.c: Ntrials=%ld Error=%10.7lf Run time (seconds)=%lf\n",
	ntrials, pi-M_PI,seconds);
}
