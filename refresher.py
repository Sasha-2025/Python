#Right Angle Star Pattern
print("Right Angle Triangle Pattern \n\n")


for i in range(1,6):

    for j in range(i):
        print("*", end="")

    print('\n')

#Inverted Star Pattern
print("Inverted Triangle Pattern \n\n")


for i in range(6,1,-1):

    for j in range(i, 1, -1):
        print("*", end="")

    print('\n')