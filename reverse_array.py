arr=[5,7,1,6,2,3,5,9]
def func(left,right):
    mid=(left+right)//2
    if left>mid+1:
        return arr
    temp= arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    return func(left+1,right-1)
print(func(2,5))
