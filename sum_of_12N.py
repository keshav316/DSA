def func(i,N,sum=0):
    if i>N:
        print(sum)
        return
    func(i+1,N,sum+i)
func(1,5)