// Find repeating elements in an aaray
#include<stdio.h>

void sortArr(int arr[], int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }

    }
}

void findRepeat(int arr[], int n){
    for(int i=0;i<n;i++){
        int flag = 0;
        while(i<n-1 && arr[i] == arr[i+1]){
            flag = 1;
            i++;
        }
        if(flag){
            printf("%d",arr[i-1]);
        }
    return;
    }

}



int main(){
    int arr[] = {1,6,6,3,1};
    // Number of elemnts in the array
    int n = sizeof(arr)/sizeof(arr[0]);
    sortArr(arr,n);
    findRepeat(arr,n);

    return 0;
}