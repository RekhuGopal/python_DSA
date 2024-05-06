arr =  [2, 44, 55, 3, 87, 8, 54, 83, 23]

n = len(arr)
i = 0

while i <= ((n//2)-1):
    arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
    i +=1

print(arr)