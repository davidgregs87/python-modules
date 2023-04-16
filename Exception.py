def safe_print_list(my_list=[], x = 0):
    index = 0
    while True:
        try:
            if (index < x):
                print(my_list[index] , end=" ")
                index += 1
            else:
                print()
                return index
        except IndexError:
            print()
            return index
    
new = safe_print_list(['banana','apple','grape','pear','mango'],1)
print(new)



