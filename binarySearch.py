def BinarySearch(arr, target):
    length = len(arr)
    left = 0
    right = length - 1
    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
result = BinarySearch([1, 2, 3, 4, 5], 5)
print(result)

# USING RECURSION

 
def binary_search(arr, target, left, right):
    mid= (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
ans = binary_search([1, 2, 3, 4, 5], 1, 0, len([1, 2, 3, 4, 5]) - 1)
print(ans)
