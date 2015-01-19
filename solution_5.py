#Week 2 homework
#Question 5
#Robert Alef

import math

def main():
    even = 2
    x = eval(input("enter a whole number (n > 2) and see if it's prime: "))
    y = int(math.sqrt(x))

    for i in range(even, y+1):
        if x % i == 0:
            print("not prime")
            break 
    else:
        print("prime")

main()
