# Lower Bound: means smallest index such that ->  nums[i] > Target

def lowerBound(arr, target):
    left = 0 
    n = len(arr)
    Right = n -1
    lb = n
    while left <= Right:
        mid = (left + Right) // 2
        if arr[mid] >= target:
            lb = mid
            Right = mid - 1
        else:
            left = mid + 1
    return lb
result = lowerBound([1,1,1 ,2, 3, 4, 5,8,8], 8)
print(result)

# Upper Bound: means smallest index such that ->  nums[i] > Target

def upperBound(arr, target):
    left = 0 
    n = len(arr)
    Right = n -1
    ub = n
    while left <= Right:
        mid = (left + Right) // 2
        if arr[mid] > target:
            ub = mid
            Right = mid - 1
        else:
            left = mid + 1
    return ub
result = upperBound([1,1,1 ,2, 3, 4, 5,8,8], 8)
print(result)