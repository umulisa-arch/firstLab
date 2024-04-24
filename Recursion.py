
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
# print("The powe of this is:L ", power(2, -2) )


print("Here is the third one:\n")

def interleave(list1, list2):
    if(len(list1) == 0):
        return list2
    elif(len(list2) == 0):
        return list1
    else:
        return [list1[0], list2[0]] + interleave(list1[1:], list2[1:])
    
print("The output will be: \n ", interleave([2,4,5], [4,6,7,10]))

print("Here is the forth one: \n")

def sumToN(n):
    if n == 0:
        return 0
    else:
        return n + sumToN(n-1)

n = int(input("Enter value of n: "))    
print(f"Here is the sum to {n}: ", sumToN(n))

print("Here is the fith one: ")
# def reverseList()