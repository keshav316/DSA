nums=[1,1,0,1,1,1]
n= len(nums)
# max_count=0
# count=0
# i=0
# while nums[i]==1:
#         count+=1
#         i+=1
# if nums[i]!=1:
#         previous_count=count
#         count=0
# if previous_count>count:
#         max_count=previous_count
# else:
#         max_count=count
# print(max_count)

count=0
max_count=0
for i in range(n):
        if nums[i]==1:
                count+=1
        elif i == n-1 and nums[i]==1:
                if max_count<count:
                        max_count=count
        else:
                if max_count<count:
                        max_count=count 
                count=0

print(max_count)
