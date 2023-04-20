from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size,size,x,y,id)

    def __str__(self) -> str:
        return(str("[{}] ({:d}) {:d}/{:d} - {:d}".format
                    (__class__.__name__,self.id,self._x,self._y,self._width)))
    @property
    def size(self):
        return self.width
    @size.setter
    def size(self,value):
        self.width = value
        self.height = value 
    def update(self, *args, **kwargs):
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key,value in kwargs.items():
                if hasattr(self,key) is True:
                    setattr(self,key,value)
    def to_dictionary(self):
        return({"id":self.id,"size":self.size,"x":self.x,"y":self.y})
