class Rectangle():

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def Rectangle_area(self):

        return   self.length*self.width




newRectangle = Rectangle(12, 10)
print('length' , newRectangle.length , 'width ' , newRectangle.width)