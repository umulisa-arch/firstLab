# work1
def myMultiplication():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    return a*b+c

print(" the result is: ")
myMultiplication()

#work2
def isOdd(x):
    result = (x%2!=0)
    
    print("Is this number odd(",  x ,")?=", result)
    return result
isOdd(13)
    

