nums = [5,6,7,7,1,9,111,1,1,5,1,1]
dict1={}
for i in nums:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1 
        
print(dict1)