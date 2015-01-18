#Week 2 homework
#Question 4
#Robert Alef

x = int(input("Enter a number to begin our Syracuse sequence "))

while x != 1:
    if x % 2 == 0:  
        x = x/2
        print(x)
    else:
        x = 3*x +1
        print(x)

print("Seems to always come back to 1!")


