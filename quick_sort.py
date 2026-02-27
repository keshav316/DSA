nums = [4,6,1,3,2,7]

def partition(nums, low, high):
    pivot = nums[low]
    i = low + 1
    j = high
    
    while True:
        # Move i right
        while i <= j and nums[i] <= pivot:
            i += 1
        
        # Move j left
        while nums[j] > pivot:
            j -= 1
        
        # Stop when pointers cross
        if i >= j:
            break
        
        nums[i], nums[j] = nums[j], nums[i]
    
    # Place pivot in correct position
    nums[low], nums[j] = nums[j], nums[low]
    return j  


def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)


quick_sort(nums, 0, len(nums) - 1)
print(nums)