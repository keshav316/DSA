arr = [1,5,6,2,4,8,9]
n=len(arr)
for i in range(0,n):
    for j in range(1,n):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
print(arr)