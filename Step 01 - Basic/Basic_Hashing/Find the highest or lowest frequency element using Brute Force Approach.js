class FrequencyCounter {
    countFreq(arr) {
        const n = arr.length;
        const visited = new Array(n).fill(false); // Track if element is already processed
        let maxFreq = 0, minFreq = n;             // Initialize min and max frequency
        let maxEle = 0, minEle = 0;               // Initialize elements

        for (let i = 0; i < n; i++) {

            // Skip already processed element
            if (visited[i]) continue;

            // Count how many times arr[i] appears
            let count = 1;
            for (let j = i + 1; j < n; j++) {
                if (arr[i] === arr[j]) {
                    visited[j] = true;  // Mark this index as processed
                    count++;
                }
            }

            // Check if this element has max frequency
            if (count > maxFreq) {
                maxEle = arr[i];
                maxFreq = count;
            }

            // Check if this element has min frequency
            if (count < minFreq) {
                minEle = arr[i];
                minFreq = count;
            }
        }

        // Output the result
        console.log("The highest frequency element is:", maxEle);
        console.log("The lowest frequency element is:", minEle);
    }
}

// Create an instance and run
const fc = new FrequencyCounter();
const arr = [10, 5, 10, 15, 10, 5]; // Sample input
fc.countFreq(arr);                 // Call method to compute frequencies
