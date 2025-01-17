def counting_sort(arr):
    # initialize frequency array with zeros
    c = [0] * 100

    # calculate frequencies
    for i in range(len(arr)):
        c[arr[i]] +=1

    # rebuild the array according to frequencies
    j = 0
    for i in range(100):
        while c[i] > 0:
            arr[j] = i
            j += 1
            c[i] -= 1

    return arr

arr = [4, 2, 2, 8, 3, 3, 1, 12]
r = counting_sort(arr)
print("Sorted array is:", r)