second_larg= float('-inf')
largest_num= float('-inf')
nums= [3, 1, 4, 1, 5, 89,9]
n= len(nums)
for num in nums:
    if num>largest_num:
        second_larg= largest_num
        largest_num= num
    elif num>second_larg and num!=largest_num:
        second_larg= num
print(second_larg)