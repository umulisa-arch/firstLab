l = (2,5,7,11)
def listSum(L):
    if len(L)==0:
        return 0
    else:
        return L[0]+listSum(L[1:])
    
print("Sum will be:", listSum([1,2,3,4,5]))
print("sum will be:", listSum([2,3,5,7,11]))
        