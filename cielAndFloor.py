def CielAndFloor(arr : list[int] , target : int):
    n = len(arr)
    left = 0
    right= n-1
    ciel=-1
    floor=-1

    while(left <= right):
        mid = (left + right) //2
        if arr[mid] == target:
            ciel = arr[mid]
            floor = arr[mid]
            return [floor, ciel]
        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1
        elif arr[mid] > target:
            ciel = arr[mid]
            right = mid - 1
        else:
            print("invalid input")
    return [floor, ciel]
result = CielAndFloor([1, 2, 4, 4, 5], 3)
print(result)