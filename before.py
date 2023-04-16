mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
mat2 = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]

print([list(map(lambda x,y:(x * y), row,col)) for row in mat for col in mat])

my_func = lambda x: round(x/3,2)
print(my_func(1))

mod_func = lambda x: 5 % x
print(mod_func(2))

func = lambda first,last: return("My name is {} {}".format(first,last))
print(func("David","Gregs"))