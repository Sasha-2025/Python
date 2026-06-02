import sys


def initial_phonebook():
    rows, columns = int(input("Please ente initial number of contacs: ")), 5


    phone_book =[]
    print(phone_book)



for i in range(rows):# 5 : 0,1,2,3,4,5 

    print("\nEnter contact %d details in the following order (ONLY):" % (i+1))

    print("NOTE: * indicates mandatory fields")

    print("....................................................................")
    temp =[]

    for j in range(cols):

        if j == 0:
            temp.append(str(input("Enter name*: ")))  

            if temp[j] == ''or temp[j] ==' ':
                sys.exit("Name is a mandatory field. Process exiting due to blank field...")  
        
        if j == 1:
            temp.append(str(input("Enter name*: ")))

        if j == 2:
            temp.append(str(input("Enter e-mail address*: ")))

            if temp[j] == ''or temp[j] ==' ':
                temp[j] = None

        if j == 3:
            temp.append(str(input("Enter date of birth(dd/mm/yy): ")))

            if temp[j] == ''or temp[j] ==' ':
                temp[j] = None

        if j == 4:
            temp.append(str(input("Enter category(Familt]y/Frieds/Work/Others): ")))

            if temp[j] == ''or temp[j] ==' ':
                temp[j] = None

    phone_book.append(temp)
        

print(phone_book)
return phone_book