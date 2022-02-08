#include <stdio.h>
#include <stdlib.h>
#define a 5000
// #define m 3
// #define n 3
// #define p 3
// #define q 3
/* 
This code takes approximatly 5min to run on device with following config-
     *-memory
          description: System memory
          physical id: 0
          size: 8GiB
     *-cpu
          product: Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz
          vendor: Intel Corp.
          physical id: 1
          bus info: cpu@0
          size: 3005MHz
          capacity: 3100MHz
          width: 64 bits
*/ 
int A[2000][2000], B[2000][2000], M[2000][2000];
int m,n,p,q;

void matrixmulti(void)
{
  // printf("\n\n");
  // for(int i = 0; i < 3; i++)
  // {
  //   for(int j = 0; j < 3; j++)
  //   {
  //     printf("%d\t",*(*(A+i)+j));
  //   }
  //   printf("\n");
  // }
  // printf("\n\n");
  // for(int i = 0; i < 3; i++)
  // {
  //   for(int j = 0; j < 3; j++)
  //   {
  //     printf("%d\t",B[i][j]);
  //   }
  //   printf("\n");
  // }
  // printf("\n\n");
  for (register int c = 0; c < m; c++) {
        for (register int k = 0; k < p; k++) {
          register int* temp2 = *(B+k);
          register int  temp = *(*(A +c) +k);
          for (register int d = 0; d < q; d++) {
            M[c][d] += temp* *(temp2+d);
          }
        }
      }
}
int rand(void);
int main()
{
  time_t t;
  
  /* Intializes random number generator */
  srand((unsigned) time(&t));

//Input
scanf("%d %d %d %d",&m,&n,&p,&q);

  // scanf("%d%d", &m, &n);
 printf("Elements of first matrix\n");
  for (register int c = 0; c < m; c++){
    for (register int d = 0; d < n; d++){
      // scanf("%d", &A[c][d]);
      A[c][d] = (rand() % 600);
      printf("%d\t",*(*(A+c)+d));
    }
    printf("\n");
  }
 
  //  scanf("%d%d", &p, &q);
 
  if (n != p)
    printf("The multiplication isn't possible.\n");
  else
  { 
    printf("Elements of second matrix\n");
    for (register int c = 0; c < p; c++){
      for (register int d = 0; d < q; d++){
      // scanf("%d", &B[c][d]);
      B[c][d] = (rand() % 600);
      printf("%d\t",*(*(B+c)+d));
    }
    printf("\n");
    }

// Matrix Multiplication 
  matrixmulti();
    printf("Product of the matrices:\n");
 
    for (register int c = 0; c < m; c++) {
      for (register int d = 0; d < q; d++)
        printf("%d\t", *(*(M+c)+d));
      printf("\n");
    }
  }
 
  return 0;
}