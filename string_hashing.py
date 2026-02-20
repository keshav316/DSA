s="azjhuiglksdghahfef"
q=['d','a','y','x']
hash_list = [0]*27
for ch in s:
    ascii_value = ord(ch)
    index = ascii_value -97
    hash_list[index]+=1
for al in q:
    ascii_value = ord(al)
    index = ascii_value -97
    print(hash_list[index])