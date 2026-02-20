# print x n times without using loop  through recursion 

count=0
def printX_Ntimes(x,n):
    global count
    if count==n:
        return 
    print(x)
    count+=1
    printX_Ntimes(x,n)
    
printX_Ntimes("Keshav",7)

# print x n times without using loop, count and global variable 

def func(x,n):
    if n==0:
        return 
    print(x)
    func(x,n-1)
func(0,2)

# print 1 to n using Recursion  using single parameter
def counting(n):
    global temp
    if n==0:
        
        return 
    print(temp-(n-1))
    n-=1
    counting(n)
n=3
temp =n
counting(n)