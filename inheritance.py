def lookup(obj):
    return(dir(obj))

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(str))

class MyList(list):
    """Subclass of the parent class List"""
    def print_sorted(self):
        return(sorted(self))  #Sorted is a function that arranges a sequence in an ascending order 

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
print(my_list.print_sorted())
print(my_list)

def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
    
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

def is_kind_of_class(obj, a_class):
    if isinstance(obj,a_class):
        return True
    else:
        return False
    
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

def inherits_from(obj, a_class):
    if issubclass(type(obj),a_class) and type(obj) != a_class :
        return True
    else:
        return False
    
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

class BaseGeometry:
    pass

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
print(dir())

class BaseGeometry:
    def __init__(self):
        pass
    def area(self):
        raise Exception("area() is not implemented")
    
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

class BaseGeometry:
    pass

    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
    
        if type(value) != int:
            raise TypeError("{} <name> must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} <name> must be greater than 0".format(name))
        
bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

class Rectangle(BaseGeometry):
    def __init__(self,width,height):
        self.integer_validator = ("width",width)
        self._width = width
        self.integer_validator = ("height", height)
        self._height = height

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

class Rectangle(BaseGeometry):
    def __init__(self,width,height):
        self.integer_validator = ("width",width)
        self._width = width
        self.integer_validator = ("height", height)
        self._height = height
    def area(self):
        print(self._width * self._height)
        return(str("[Rectangle] {} / {}".format(self._width,self._height)))


r = Rectangle(3, 5)

print(r)
print(r.area())   

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator = ("size",size)
        self._size = size
    def area(self):
        print(self._size * self._size)
        return(str("[Rectangle] {} / {}".format(self._size,self._size)))
    
s = Square(13)

print(s)
print(s.area())

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator = ("size",size)
        self._size = size
    def area(self):
        print(self._size * self._size)
        return(str("[Square] {} / {}".format(self._size,self._size)))

s = Square(13)

print(s)
print(s.area())

class MyInt(int):
    def __eq__(self, __value: object) -> bool:
        return(False)
    def __ne__(self, __value: object) -> bool:
        return(True)

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)