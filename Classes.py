"""""class Person:
    def greeting(self):
        return("How are you doing") # Simple example on how to create a class

print(Person().greeting())"""""

"""class Person:
    def __init__(self,name):
        self.name = name
        
    def say_hi(self):
        return('my name is {}'.format(self.name)) 

print(Person("Andres").say_hi())"""  

"""class Square:
# An empty Class Square
    pass
a = Square()  
print(type(a))
print(a.__dict__)"""

"""class Square:
    # Instantiante a private attribute "size"
    def __init__(self,size):
        self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)"""

"""class Square:
    def __init__(self,size=0):
        
        if size < 0:
            raise ValueError ("size must be >= 0")
        elif type(size) is not int:
            raise TypeError ("size must be an integer")
        self.__size = size

a = Square(3)
print(type(a))
print(a.__dict__)

b = Square()
print(type(b))
print(b.__dict__)

try:
    print(a.size)
except Exception as e:
    print(e)

try:
    print(a.__size)
except Exception as e:
    print(e)"""

"""class Square:
    def __init__(self,size=0):
        if type(size) is not int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
    def area(self):
    
        #Return the area of a square

        return(self.__size * self.__size)
a = Square(5)
print("Area: {}".format(a.area()))"""

"""class Square:
    def __init__(self,size=0):
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")
        self.__size = value 

    def area(self):
        return (self.__size * self.__size)
try:    
    a = Square()
    print("Area: {}\nFor size: {}".format(a.area(),a.size))
except Exception as e:
    print(e)"""

"""class Square:
    def __init__(self,size=0):
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        if type(value) is not int:
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")
        self.__size = value 
    def area(self):
        return(self.__size*self.__size)
    def my_print(self):
        if self.__size != 0:
            for x in range(0, self.__size):
                [print("#", end="") for y in range(self.__size)]
                print("")
                
        else:
            print("--")

a = Square(3)
print("{}".format(a.my_print()))"""

"""class Square:
    def __init__(self,size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        if type(value) is not int:
            raise TypeError ("Value must be an integer")
        else:
            pass
        if value < 0:
            raise ValueError ("Value must be >= 0")
        else:
            pass

    def area(self):
        # Calculate the area of a square
        return(self.__size * self.__size)
    
    def __eq__(self, other):
        # Compare square sizes
        return(self.area() == other.area())
    def __lt__(self, other):
        return(self.area() < other.area())
    def __gt__(self, other):
        return(self.area() > other.area())
    def __le__(self, other):
        return(self.area() <= other.area())
    def __ge__(self, other):
        return(self.area() >= other.area())
    def __ne__(self, other):
        return(self.area() != other.area())
    

s1 = Square(4)
s2 = Square(6)

if s2 !=  s1:
    print("Correct")
else:
    print("Incorrect")"""

class Triangle:
    """This is a Triangle class"""
    def __init__(self,base,height):
        self.base = base
        self.height = height

        if base <= 0 and height <= 0:
            raise ValueError ("both attributes must be > 0")
        if type(base) != int or type(height) != int:
            raise TypeError ("both attributes muust be of type integer")
        
    def Area(self):
        """Returns the area of a triangle"""
        return (1/2 * self.base * self.height)

    
s = Triangle(2,"g")
print(s.Area())

