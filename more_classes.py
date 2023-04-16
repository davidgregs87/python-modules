"""class Rectangle:
    #An empty class that defines a rectangle
    pass

p = Rectangle()
print(type(p))
print(p.__dict__)"""

"""class Rectangle:
    #Real definition of a rectangle
    def __init__(self,width=0,height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

p = Rectangle(2,3)
print(p.__dict__)
p.width = 5
p.height = 7
print(p.__dict__)"""

"""class Rectangle:
    def __init__(self,width=0,height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        return(self.__width * self.__height)
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return(2 * (self.__width + self.__height))
    

p = Rectangle(2,4)
print("Area: {} - Perimeter: {}".format(p.area(),p.perimeter()))
p.width = 10
p.height = 0
print("Area: {} - Perimeter: {}".format(p.area(),p.perimeter()))"""

class Rectangle:
    def __init__(self,width=0,height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        return(self.__width * self.__height)
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return(2 * (self.__width + self.__height))
    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    string += "#"
                string += "\n"
            string = string[:-1]
            return (string)
    def __repr__(self):
        wid = str(self.__width)
        hei = str(self.__height)
        return "Rectangle(" + wid + ", " + hei + ")"
    def __del__(self):
        print("Goodbye...")
    
p = Rectangle(2,4)
print("Area: {} - Perimeter: {}".format(p.area(),p.perimeter()))
print(str(p))
print(p)
print(repr(p))
print(hex(id(p)))

d =eval(repr(p))
print(str(d))
print(d)
print (repr(d))
print(hex(id(d)))
print(p is d)
print(type(p) is type(d))
print(type(p))

del p
try:
    print(p)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))



    




        
        