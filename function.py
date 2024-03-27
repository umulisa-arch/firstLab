def summation(n1, n2):
    sum = n1+n2
    print("sum of 2 numbers: ", sum)
summation(20,19)

def isPositive(n):
    result = (n>0)
    print("isPositive(",  n ,")=", result)
    return result
isPositive(-10)

def isEven(n):
    result = (n%2==0)
    print("isEven(",  n ,")=", result)
    return result
isEven(13)
