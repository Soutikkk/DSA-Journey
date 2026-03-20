class Solution {
    // Function to count frequency of each element in the array using Map
    Frequency(arr, n) {
        // Create a Map to store frequency of each element
        const map = new Map();

        // Traverse the array and count frequencies
        for (let i = 0; i < n; i++) {
            map.set(arr[i], (map.get(arr[i]) || 0) + 1);
        }

        // Traverse through the Map and print frequencies
        map.forEach((value, key) => {
            console.log(key, value);
        });
    }
}

// Driver code
(function main() {
    // Input array
    const arr = [10, 5, 10, 15, 10, 5];
    const n = arr.length;

    // Create Solution instance
    const sol = new Solution();

    // Call the function to count frequencies
    sol.Frequency(arr, n);
})();
