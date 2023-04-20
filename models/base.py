import json
import csv



class Base:
    """A class called Base"""

    __nb_objects = 0

    def __init__(self,id=None,):

        """Initializing id"""
        
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return (json.dumps(list_dictionaries))
    @classmethod
    def save_to_file(cls, list_objs):
        fname = cls.__name__ + '.json'
        my_list = []
        if (list_objs is not None):
            for args in list_objs:
                my_list.append(args.to_dictionary())
            my_dict = cls.to_json_string(my_list)
            with open(fname,"w") as f:
                f.write(my_dict)
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0: 
            return "[]"
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        if (cls.__name__ == 'Rectangle'):
            dummy = cls(1, 2)
        elif (cls.__name__ == 'Square'):
            dummy = cls(3)
        dummy.update(**dictionary)
        return (dummy)
    @classmethod
    def load_from_file(cls):
        fname = cls.__name__ + '.json'
        try:
            with open(fname,"r") as f:
                load = cls.from_json_string(f.read())
                return(cls.create(**d) for d in load)
        except FileNotFoundError:
            return "[]"
    @classmethod
    def save_to_file_csv(cls, list_objs):
        fname = cls.__name__ + '.csv'
        for args in list_objs:
            with open(fname,"w") as f:
                return f.write(csv.DictWriter(args))
    @staticmethod
    def draw(list_rectangles, list_squares):
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()



            

                
        




