# This is my TTD project's source code
"""def  add_integer(a,b=98):
    if type(a) is not int and type(b) is not int:
        raise TypeError ("a must be an integer or b must be an integer")
    
    return int(a+b)
    
print(add_integer(1,2))
print(add_integer(100,-2))
print(add_integer(2))
print(add_integer(100.3,-2))
try:
    print(add_integer(4,"school"))
except Exception as e:
    print(e)

try:
    print(add_integer(None))
except Exception as e:
    print(e)"""

"""def matrix_divided(matrix,div):
    if not isinstance(matrix, list) or matrix == []:
        if not all(isinstance(row,int) for row in matrix) or not all((isinstance(ele,float) or not all(isinstance(ele, int)) for ele in[num for row in matrix for num in row])):
            raise TypeError("matrix must be a (list of list) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x/div,2),row)) for row in matrix])        

s = [
    [1,2,3],
    [4,5,6]
]
print(matrix_divided(s,3))"""

def say_my_name(first_name,last_name=""):
    """Returns the first and last name of the user"""

    if not isinstance(first_name, str):
        raise TypeError("firstname must be a string")
    if not isinstance(last_name,str):
        raise TypeError("lastname must be a string")

    return("my name is {} {}".format(first_name,last_name))

"""print(say_my_name("bob"))
try:
    print(say_my_name("sam",11))
except Exception as e:
    print(e)"""