from base import Base

                            #Assign each argument to the right attribute means using setters and getters
                            #Why private attributes with getter/setter? Why not directly public attribute?
                            #Because we want to protect attributes of our class
                            #With a setter, you are able to validate what a developer is trying to assign to a variable.
                            #So after, in your class you can “trust” these attributes.
class Rectangle(Base):
    
    def __init__(self,width,height,x=0,y=0,id=None):
        self._width = width   
        self._height = height
        self._x = x
        self._y = y
        
        super().__init__(id)
    @property                         
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    @property
    def x (self):
        return self._x
    @x.setter
    def x(self,value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value
    @property
    def y (self):
        return self._y
    @y.setter
    def y(self,value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value
    def area(self):
        return self._width * self._height
    def display(self):
        for i in range(self._width):
            print("" "#" * self._height)
    def __str__(self) -> str:
        return(str("[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                    (__class__.__name__,self.id,self._x,self._y,self._width,self._height)))
    def update(self, *args,**kwargs):
        if len(args):
            for i,arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key,value in kwargs.items():
                if hasattr(self,key) is True:
                    setattr(self,key,value)
    def to_dictionary(self):
        return({"id":self.id,"width":self.width,"height":self.height,"x":self.x,"y":self.y})



