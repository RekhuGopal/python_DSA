def shift_list_right(arr, k):
    k = k % len(arr)
    print(arr[-k:])
    print(arr[:-k])
    return arr[-k:] + arr[:-k]

arr = [1,2,3,4,5,6,7]
k = 3
arr_shifted = shift_list_right(arr, k)
print(arr_shifted)