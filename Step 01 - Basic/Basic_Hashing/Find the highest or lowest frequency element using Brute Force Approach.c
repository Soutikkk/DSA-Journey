#include <stdio.h>
#include <stdbool.h>

void countFreq(int arr[], int n) {
    bool visited[n];   // Track visited elements

    // Initialize visited array
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }

    int maxFreq = 0;
    int minFreq = n;
    int maxEle = 0;
    int minEle = 0;

    for (int i = 0; i < n; i++) {

        // Skip already processed elements
        if (visited[i] == true)
            continue;

        int count = 1;

        // Count frequency of arr[i]
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                visited[j] = true;
                count++;
            }
        }

        // Update max frequency
        if (count > maxFreq) {
            maxFreq = count;
            maxEle = arr[i];
        }

        // Update min frequency
        if (count < minFreq) {
            minFreq = count;
            minEle = arr[i];
        }
    }

    printf("The highest frequency element is: %d\n", maxEle);
    printf("The lowest frequency element is: %d\n", minEle);
}

int main() {
    int arr[] = {10, 5, 10, 15, 10, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    countFreq(arr, n);

    return 0;
}