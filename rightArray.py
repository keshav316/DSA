nums=[7,5,-2,3,9,10,6,10,7]
# length=len(nums)
# rotate= 2
# still= nums[0:length-rotate]
# agea= nums[length-rotate:]
# print(agea+still)

n= len(nums)
temp= nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)
