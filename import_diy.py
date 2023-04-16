from TDD import say_my_name
import sys
import os

print(say_my_name("sam","frank"))

to_json_string = __import__ ("Input_Output").to_json_string

my_list = [1,2,3]
s = to_json_string(my_list)
print(s)
print(type(s))

my_dict = {'ID':12,'name':"John",'places':["San Francisco", 
            "Tokyo"],'is_active':True,'info':{'age':36,'average':3.14}}
s_dict = to_json_string(my_dict)
print(s_dict)
print(type(s_dict))


try:
    my_set = {132,2}
    d = to_json_string(my_set)
    print(d)
    print(type(d))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))

from_json_string = __import__("Input_Output").from_json_string
a_list = "[1,2,3]"
a = from_json_string(a_list)
print(a)
print(type(a))

a_dict = """{"ID":12,"name":"John","places":["SanFrancisco"
,"Tokyo"],"is_active":true,"info":{"age":36,"average":3.14}}"""
f = from_json_string(a_dict)
print(f)
print(type(f))

save_to_json_file = __import__("Input_Output").save_to_json_file

filename = "my_list.json"
num = [1,2,3]
save_to_json_file(num,filename)

filename = "my_dict.json"
item = {'ID':12,'name':"John",'places':["San Francisco", 
            "Tokyo"],'is_active':True,'info':{'age':36,'average':3.14}}
save_to_json_file(item,filename)

try:
    filename = "my_set.json"
    param = {132,2}
    save_to_json_file(param,filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))

load_from_json_file = __import__("Input_Output").load_from_json_file

filename = "my_list.json"
a = load_from_json_file(filename)
print(a)
print(type(a))
filename = "my_dict.json"
b = load_from_json_file(filename)
print(b)
print(type(b))

try:
    filename = "file_dosen't_exist.json"
    c = load_from_json_file(filename)
    print(c)
    print(type(c))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))
try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__,e))

#
class_to_json = __import__("Input_Output").class_to_json
class MyClass:
    def __init__(self,name):
        self.name = name
        self.number = 0
    def __str__(self):
        return"[MyClass] {} - {:d}".format(self.name,self.number)
    
m = MyClass("John")
m.number = 89
print(type(m))
print(m)

d = class_to_json(m)
print(type(d))
print(d)

c = m.__dict__
print(type(c))
print(c)

#    
Student = __import__("Input_Output").Student
read_file = __import__("Input_Output").read_file

students = [Student("John","Doe",27),Student("Bob","Dylan",23)]
for student in students:
    f = student.to_json()
    print(type(f))
    print(f["first_name"])
    print(type(f["first_name"]))
    print(f["age"])
    print(type(f["age"]))

v = Student("john","doe",32)
b = v.to_json()
print(type(b))
save_to_json_file(b,"new_file.json")
print(read_file("new_file.json"))
print("\nSaved to current working directory")
s1 = Student("fake","fake",30)
b2 = load_from_json_file("new_file.json")
s1.reload_from_json(b)
print(s1)

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


