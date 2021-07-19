def largestSum(arr):
    if len(arr) == 0:
        return 0
    
    maxSum = currentSum = arr[0]

    for num in arr[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(maxSum, currentSum)

    return maxSum

if __name__ == "__main__":
    assert largestSum([7,1,2-1,3,4,10,-12,3,21,-19]) == 38, "Failed test case."