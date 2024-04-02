def gcd(x, y):
    if y == 0:
        return x
    else:
        
        return gcd(y, x % y)

x = int(input("Enter the first positive integer (x): "))
y = int(input("Enter the second positive integer (y): "))

if x > 0 and y > 0:
    
    print("The greatest common divisor (GCD) of", x, "and", y, "is:", gcd(x, y))
else:
    print("Invalid input. Please enter positive integers.")