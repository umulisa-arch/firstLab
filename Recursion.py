
def listSum(L):
    if len(L)==0:
        return 0
    else:
        return L[0]+listSum(L[1:])
    
print("Sum will be:", listSum([1,2,3,4,5]))
print("sum will be:", listSum([2,3,5,7,11]))
print("sum will be:", listSum([]))
        


print("Second one")

def power(base: int, exp: int):
    if (exp == 0):
        return 1
    else:
        return base * power (base, exp-1)

print("The power will be: ", power(2, 6))
