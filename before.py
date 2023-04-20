def arg_list(*args,**kwargs):
    if len(args):
        for num,arg in enumerate(args):
            print(str("{}.{}".format(num,arg)))
    elif kwargs is not None:
        for key,value in kwargs.items():
            print("{}:{}".format(key,value))        
    
print(arg_list(name = "david",id = 44,occupation = "student", dept = "statistics"))
print(arg_list("Messi",35,"left","PSG"))

a = []
print(len(a))