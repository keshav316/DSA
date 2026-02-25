def merge_SortedArray(left, Right):
    result = []
    n,m = len(left), len(Right)
    i = j = 0
    while i < n and j < m:
        if left[i] <= Right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(Right[j])
            j += 1
    if i < n:
        while(i < n):
            result.append(left[i])
            i += 1
    if j < m:
        while(j < m):
            result.append(Right[j])
            j += 1
    return result
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge_SortedArray(left_arr, right_arr)
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))