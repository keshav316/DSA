nums=[3,4,5,6,7,8,9,10,7,1]

for i in range(1,len(nums)):
    key=nums[i]
    j=i-1
    while j>=0 and key<nums[j]:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key