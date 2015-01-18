#Week 2 homework
#Question 5
#Robert Alef

import math
even = 2
x = eval(input("enter a number and see if it's prime "))
y = int(math.sqrt(x))

for i in range(even, y+1):
    if x % i == 0:
        print("not prime")
        break 
else:
    print("prime")
