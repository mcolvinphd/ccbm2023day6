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
  double sum=0, seconds;
  long i;
  clock_t begin, end;
  begin=clock();
  for (i=0; i<=ntrials; i++) {
    double x=i;
    sum+=sqrt(x);
  }
  end=clock();
  seconds=(double)(end-begin)/CLOCKS_PER_SEC;
  printf("sumsqrt.c: Sum sqrt first %ld numbers= %15.7lf time= %lf\n",ntrials,sum,seconds);
}
