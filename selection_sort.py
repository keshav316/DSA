arr=[5,7,8,4,1,6,9,2]
for i in range(0,len(arr)):
    min_index= i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index = j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
 