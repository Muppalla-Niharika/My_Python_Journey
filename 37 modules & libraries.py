'''from Calc import *
#math module
a = 9
b = 12
c = sub(a,b)
print(c)

#math module
import math
print(math.pi)
print(math.sqrt(5))
print(math.ceil(4.2))
print(math.floor(5.9))
print(math.pow(2,12))

#random module
import random
fruits = ["apple","banana","pineapple"]
print(random.random())
print(random.randint(1,15))
print(random.choice(["apple","banana","pineapple"]))
random.shuffle(fruits)
print(fruits)


#datetime module
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)              # current month
print(now.day)                # current day
print(now.strftime("%d/%m/%Y"))  # formatted date!
'''
import math
print(math.sqrt(4))
from math import sqrt
print(sqrt(4))
import math as m
print(m.sqrt(4))


import math

print(math.ceil(4.2))
print(math.floor(4.9))


from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)

from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
































































