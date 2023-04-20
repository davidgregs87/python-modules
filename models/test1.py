from base import Base
from Rectangle import Rectangle
from Square import Square

list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

Base.draw(list_rectangles, list_squares)