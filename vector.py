class Vector:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def gety(self):
        return self.__y

    def sety(self, value):
        self.__y = value

    x = property(getx, setx)
    y = property(getx, setx)

    def __str__(self):
        return "Vector(" + str(self.__x) + ", " + str(self.__y) + ")"

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        return Vector(self.__x * other, self.__y * other)

    def __neg__(self):
        return Vector(self.__x * -1, self.__y * -1)

    def opposite_x(self):
        self.__x *= -1

    def opposite_y(self):
        self.__y *= -1
