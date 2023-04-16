import pathlib as path
def food(f_s,*args):
    print("I love {}".format(f_s))
    for arg in args:
        print("I love {}".format(arg))

print(food("rice","beans","yam","indomie","eggs"))

def test_args(arg1,arg2,arg3):
    print("This is {}".format(arg1))
    print("I am in {} dept".format(arg2))
    print("Staff ID {}".format(arg3))

print_args = ("cup","pot","kettle")
print(test_args(*print_args))
b = {"arg1":"Sam","arg2":"HR","arg3":44}
print(test_args(**b)
      )
def Test_for_Uppercase(text=""):
    return str.isupper(text)
        

print(Test_for_Uppercase("DAVID"))
