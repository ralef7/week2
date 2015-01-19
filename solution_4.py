#Week 2 homework
#Question 4
#Robert Alef

def main():
    try:
        x = int(input("Enter a natural number to begin our Syracuse sequence "))

        while x != 1:
            if x % 2 == 0:  
                x = x/2
                print(x)
            else:
                x = 3*x +1
                print(x)

        print("Seems to always come back to 1!")

    except ValueError:
        print("\nSorry. You did not enter a natural number.  You must have entered an unnatural number lol")

main()
