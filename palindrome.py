pal=0
num= 5665
n = num
while (n>0):
    last = n%10
   
    pal = pal *10
    pal = pal +last
    print(pal)
    n = n//10
    
if pal ==+ num:
    print("palindrome")
else:
    print("not Palindrome")