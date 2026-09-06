nums=[1,1,1,2,3,4,4,7,9,9,9,10]
i=0
n=len(nums)
while(i<n-1):
    if nums[i]==nums[i+1]:
        remove=nums[i+1]
        nums.pop(i+1)
        nums.append(remove)
        n-=1
    else:
        i+=1
print(nums)