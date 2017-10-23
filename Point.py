#This is a class to handle and manager multiple points.



class Point():

    def __init__(self):
        self.position = [0, 0, 0]

    def setPosition(self, x, y, z):
        self.position = x,y,z

    def printPosition(self):
        print("X: " + str(self.position[0]))
        print("Y: " + str(self.position[0]))
        print("Z: " + str(self.position[0]))

    #Returns a List of 3 points.
    def getPosition(self):
        return self.position
    def setX(self, x):
        self.position[0] = x

    def setY(self, y):
        self.position[0] = y

    def setZ(self, z):
        self.position[0] = z

    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]

    def getZ(self):
        return self.position[2]

    def setCenter(self,  center):
        self.center = center

    def getCenter(self):
        return self.center

    def setRadius(self,  radius):
        self.radius = radius

    def getRadius(self):
        return self.radius