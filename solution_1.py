#Week 2 homework
#Question 1
#Robert Alef


def Fibonacci(n):
    a = 0
    b = 1
    c = 1

    for num in range(n):
        a = b
        b = c
        c = a + b

        num -= 1

    return a
def main():
    try:
        x = eval(input("Enter integer 'n' to find out the 'nth' Fibonacci number: "))
        while x < 0:
            print("The Fibonacci sequence is not entirely clear on the existence of negative numbers")
            print("Please enter 0 or a positive integer")
            x = eval(input("Try again "))
            if x >= 0:
                print("{0} is your Fibonacci number!".format(Fibonacci(x)))
                break
        else:
            print("{0} is your Fibonacci number!".format(Fibonacci(x)))
    except TypeError:
        print("\nYour number returned a type error. Are you sure you entered an integer?")
    except NameError:
        print("\nYour input returned a name error.  Are you sure you entered an integer?")
main()



    
