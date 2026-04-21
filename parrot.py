class Parrot:


    species = "bird"


    def __init__(self, name, age): # constructor function
        self.name = name 
        self.age = age





parrotobject1 = Parrot('bluyy', 10)
parrotobject2 = Parrot('greeny', 13)

print("{} is {} years old" .format(parrotobject1.name, parrotobject1.age))

print("'Bluyy' is a {} " .format(parrotobject1.species))