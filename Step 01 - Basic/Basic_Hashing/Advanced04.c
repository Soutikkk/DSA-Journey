#include <stdio.h>

int main() {

    int arr[] = {3,5,3,2,5,5,7};
    int n = 7;

    int hash[10] = {0};   // hash table

    for(int i=0;i<n;i++)
    {
        hash[arr[i]]++;
    }

    for(int i=0;i<10;i++)
    {
        if(hash[i] != 0)
        printf("%d occurs %d times\n", i, hash[i]);
    }

    return 0;
}