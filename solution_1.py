#Week 2 homework
#Question 1
#Robert Alef

def main():
    def Fibonacci(n):
        a = 0
        b = 1
        c = 1

        for num in range(n):
            a = b
            b = c
            c = a + b

            n -= 1

        return a

    x = eval(input("Enter 'n' to find out the 'nth' Fibonacci number: "))

    print(Fibonacci(x))

main()



    
