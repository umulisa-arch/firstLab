n = "I can make it"
print(n)
# n.replace("make", 'do')
print(n.replace("make", 'do'))

#second
from types import SimpleNamespace #class
import copy
dog1 = SimpleNamespace(name='Dino', age= 12, breed='shepherd') #dog1 is an instance of class
dog2 = dog1 #alias
dog3 = copy.copy(dog1) # not alias
dog1.name = 'Spot'
print()
print(dog1)
print(dog2.name)
print(dog3.name)

#third
from dataclasses import make_dataclass

# Dog  = make_dataclass()

#forth constructor
class Dogs(object):
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def bark(self, times):
        
d1 = Dogs('Dot', 10)
d2 = Dogs('helliman', 12)
print("dog1 is:", d1)
        



