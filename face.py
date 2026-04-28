class Face:

     def __init__(self, xpos, ypos):

        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = 'small'



    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.draweye(135)
        self.draweye(45)
        self.drawmouth()
        self.drawnose()
        pensize(5)

    def goHome(self):
        penup()
        goto(self.coord)

        setheading(0)


    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        circle(self.size)
        self.goHome()    