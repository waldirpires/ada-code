class CountingSort:
    def sort(self, arr):
        # Step 1: Find the range of the input data
        max_val = max(arr)
        min_val = min(arr)
        range_of_elements = max_val - min_val + 1

        # Step 2: Initialize the count array
        freq = [0] * range_of_elements
        output = [0] * len(arr)

        # Step 3: Store the count/frequency of each element
        for num in arr:
            freq[num - min_val] += 1

        # Step 4: Calculate cumulative count
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        # Step 5: Place the elements in the sorted order
        for num in reversed(arr):
            output[freq[num - min_val] - 1] = num
            freq[num - min_val] -= 1

        # Copy the sorted elements into original array
        for i in range(len(arr)):
            arr[i] = output[i]

        return arr

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1, -1]
c = CountingSort()
r = c.sort(arr)
print("Sorted array is:", r)