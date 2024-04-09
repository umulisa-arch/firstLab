a  = [2, 6, 3, 6, 7, 8, 10, 10, 10]
c = [2, 3, 6, -8, "Hello"]
c.append(101) # adding new element at the end
c.insert(0, 120) # you speciy the index and the element tha you want to insert c.inse(index, element)
c.remove(a[1]) # removing an element from the list
c.remove(2)   # removing an element from the list
print(c)
c.pop(2) # this also means remove an element from the list
comList = [[1, 2, 3, 0], [0, 12, 100, 23],["hi", 'Hello ', "Agnes"]]
print(comList[2][1] +comList[2][2])
print(c) 
print("6 appears", a.count(6),"times") # count the numeber of times an element occurs


print(a==c)
print(a[-1]) #it gives value from last one
print(c[-1])
print(a[0:6:2]) # this is called slice 
print(a+c)
# print(a[2]+c[3])
#this is called alias
d = a 
d[0] = 12
print([d])

def f(h): 
    h[0] = 100
h =[12, 101, 122]
k = h.copy()

print(h)
print(k[2])

print("from w3schools")
l = "hello, World!"
print(l.replace("hello", 'Hi'))

name = "Rukundo"
lName = "AGNES"
print(name.upper(),"",lName.lower())