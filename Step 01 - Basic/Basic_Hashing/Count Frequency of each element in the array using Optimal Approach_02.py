from collections import defaultdict

class Solution:
    def Frequency(self, arr):
        freq_map = defaultdict(int)

        for num in arr:
            freq_map[num] += 1

        return freq_map


if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]

    sol = Solution()
    result = sol.Frequency(arr)

    for key, value in result.items():
        print(key, value)