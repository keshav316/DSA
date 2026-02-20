n=[4,5,2,5,7,8,9,9,4,8,5,0,3,8]
m =[5,7,8,2,1,9,33]
hash_list = [0]*(max(n)+1)
for num in n:
    hash_list[num]+=1
for x in m:
    if x>10 or x<1:
        print(0)
        
    else:
        print(hash_list[x])