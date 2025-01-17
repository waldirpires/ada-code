def counting_sort_for_radix(arr, exp):
    n = len(arr)

    # Initialize the output array and the count array
    output = [0] * n
    count = [0] * 10  # There are 10 possible digits (0 to 9)

    # Store the count of occurrences of each digit in the count array
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Modify the count array to store cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the cumulative counts
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the sorted elements back into the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)

    # Perform counting sort for every digit, starting from the LSD to the MSD
    exp = 1  # exp is 10^i where i is the current digit position
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array is:", arr)