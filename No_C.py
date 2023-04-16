def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            print("{}".format(my_string[i]),end="")
    

my_string = "C is fun!"
no_c(my_string)