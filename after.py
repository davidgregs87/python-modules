import sys
"""def safe_print_integer(value):  # Print out the parameter value to the console
    try:
        if value:
            return("{}".format(value))
        else:
            return(False)
    except (ValueError,TypeError):
        return("Invalid value")
    
print(safe_print_integer(-87.5))"""



"""def safe_print_division(a, b):
    try:
        c = a/b
        return(c)
    except ZeroDivisionError:        # Compute simple division,if divisor is 0 raise the ZeroDivisionError
        return("Cannot divide by zero!")
    
print(safe_print_division(8,2))
print(safe_print_division(8,0))"""


"""def list_division(my_list_1, my_list_2, list_length):
   result  = []
   for i in range(list_length):
      try:
        res =  my_list_1[i]/my_list_2[i]

      except ZeroDivisionError:  
        print("Division by 0")
        res = 0
      except TypeError:
        print("Wrong type!")
        res = 0
      except IndexError:
        print("Out of index!")
        res = 0
      finally:
        result.append(res)
   return(result)

    


ans = list_division([10,8,6,4,2],[2,4,3,2],8)
print(ans) """


"""def raise_exception():
    raise TypeError


print(raise_exception())"""


"""def raise_exception_msg(message=""):
    raise NameError(message)

print(raise_exception_msg("C is fun"))"""


"""def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError,TypeError):
        print("Exception: {}".format(sys.exc_info()[1]),file = sys.stderr)
        return(False)
    

value = "school"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))"""


"""def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError,TypeError,ZeroDivisionError,IndexError) as e: # To catch an error of a function defined by a user
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    
def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))"""