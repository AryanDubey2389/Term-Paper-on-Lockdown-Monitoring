#include <stdio.h>
#include <stdlib.h>
 
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
int arr[6000000];
int L[6000000], R[6000000];
int min(register int a, register int b)
{
    if(a < b)
        return a;
    return b;
}
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        /* Move elements of arr[0..i-1], that are
        greater than key, to one position ahead
        of their current position */
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
void merge(register int arr[],register int l,register int m,register int r)
{
    register int i, j, k;
    register int n1 = m - l + 1;
    register int n2 = r - m;
 
    /* create temp arrays */
    // int L[n1], R[n2];
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    /* Copy the remaining elements of L[], if there
    are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    /* Copy the remaining elements of R[], if there
    are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
void mergeSort(register int arr[],register  int n)
{
    register int curr_size;  
    register int left_start; 
   for (curr_size=1; curr_size<=n-1; curr_size = 2*curr_size)
   {
       // Pick starting point of different subarrays of current size
       for (left_start=0; left_start<n-1; left_start += 2*curr_size)
       {
           register int mid = min(left_start + curr_size - 1, n-1);
           register int right_end = min(left_start + 2*curr_size - 1, n-1);
           merge(arr, left_start, mid, right_end);
       }
   }
}
 
void printArray(int A[], int size)
{
    register int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

int rand(void);
 
/* Driver code */
int main()
{
    time_t t;
  
  /* Intializes random number generator */
    srand((unsigned) time(&t));
    int arr_size ;
    printf("Enter the size of array\n");
    scanf("%d", &arr_size);
    register int i=0;
    for(i = 0;i<arr_size - 16;i+=16) {
        // scanf("%d",&arr[i]);
        arr[i] = (rand() % 10000000);
        arr[i+1] = (rand() % 10000000);
        arr[i+2] = (rand() % 10000000);
        arr[i+3] = (rand() % 10000000);
        arr[i+4] = (rand() % 10000000);
        arr[i+5] = (rand() % 10000000);
        arr[i+6] = (rand() % 10000000);
        arr[i+7] = (rand() % 10000000);
        arr[i+8] = (rand() % 10000000);
        arr[i+9] = (rand() % 10000000);
        arr[i+10] = (rand() % 10000000);
        arr[i+11] = (rand() % 10000000);
        arr[i+12] = (rand() % 10000000);
        arr[i+13] = (rand() % 10000000);
        arr[i+14] = (rand() % 10000000);
        arr[i+15] = (rand() % 10000000);
    }
    for(;i<arr_size;i++)
    {
        arr[i] = (rand() % 10000000);
    }
    if(arr_size < 40)
        insertionSort(arr,arr_size);
    else
        mergeSort(arr, arr_size);
 
    printf("\nSorted array is \n");
    // printArray(arr, arr_size);
    return 0;
}   