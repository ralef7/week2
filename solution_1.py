#Week 2 homework
#Question 1
#Robert Alef

def Fibonacci(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

x = eval(input("Enter a number for our Fibonacci code "))


print(Fibonacci(x))




    
