#include <stdio.h>

void Frequency(int arr[], int n) {
    int visited[n];

    // Initialize visited array
    for(int i = 0; i < n; i++)
        visited[i] = 0;

    for(int i = 0; i < n; i++) {

        if(visited[i] == 1)
            continue;

        int count = 1;

        for(int j = i + 1; j < n; j++) {
            if(arr[i] == arr[j]) {
                count++;
                visited[j] = 1;
            }
        }

        printf("%d %d\n", arr[i], count);
    }
}

int main() {
    int arr[] = {10, 5, 10, 15, 10, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    Frequency(arr, n);

    return 0;
}