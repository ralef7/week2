#Week 2 Homework
#Question 10
#Robert Alef

def main():
    totmilesdriven = 0
    totgasused = 0
    prevodom = 0
    leg = 0
        
    filename = "driving_legs.txt"
    file = open(filename, "r")

    for line in file:
        
        odom, gals = line.split()
        

        if leg == 0:
            prevodom = odom
            leg += 1
            continue

        milesdriven = float(odom) - float(prevodom)
        mpg = milesdriven / float(gals)
        print("Leg {0}: Drove {1} miles on {2} gallons for a rate of {3:.2f} MPG".format(leg, milesdriven, gals, mpg))

        totmilesdriven += milesdriven
        totgasused += float(gals)

        prevodom = odom
        leg += 1

    totalmpg = totmilesdriven / totgasused
    print("Overall Trip Data: \n\tTotal miles driven: {0}\n\tTotal Gas Used: {1} gallons\n\tOverall fuel efficeincy: {2:.2f}MPG" .format(totmilesdriven, totgasused, totalmpg))
    file.close()          

main()
        
