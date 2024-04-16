#2D List and tuples 
c= ['hello', [1,2,3], 'python']
print(c[2])
c.insert(2, "This is week four")
print(c)
f = [6,2,2]
c.extend(f)
print(c)
print(f.index(2))# to get the position of the element
d = [0]*10
print(d)

#create new albitrary 2d list
import copy
a = [[2,3,5],[1,4,7]]
print("our a is: ", a)
print(len(a[0]))

#shalow copy 
Christiano = 37
cr7 = copy.copy(Christiano)
print(cr7)
cr7 = 40
print(cr7)
print(f"sum of {a[0][1]} and {a[1][-1]} is:  {a[0][1]+a[1][-1]}")

#and deep copy
