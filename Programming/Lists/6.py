k = 3
def mSum(arr):
    sum = 0
    for i in range(k):
        sum += arr[i]
    maxSum = sum
    for i in range(1,len(arr)-k+1):
        sum = 0
        for j in range(i,k+i):
            sum += arr[j]
        maxSum = max(maxSum,sum)
    return maxSum

arr = [8,-6,3,4,-1,6,3,-1]
print(mSum(arr))
