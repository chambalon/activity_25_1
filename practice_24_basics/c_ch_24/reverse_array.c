// Reverse an array
#include<stdio.h>

void revArr(int arr[], int n) {
    int i,j,element;
    for(i=0,j=n-1;i<j;++i,--j){
        element = arr[i];
        arr[i] = arr[j];
        arr[j] = element;
    } 
}

int main(){
    int n = 5;
    int arr[] = {1,2,3,4,5};
    revArr(arr, n);

    for(int i=0; i<n; ++i){
         printf("%d\n",arr[i]);
    }
    
return 0;
}