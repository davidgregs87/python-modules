import json,sys

def read_file(filename = ""):

    """Read the content of a file, if the file is in your current 
    working directory else replace filename with it's  full path 
     where the file exists if file is not present in the CWD  """

    with open(filename, "r") as f:
        return(f.read())
    
def write_file(filename = "" , text = ""):
    """This function should write a string to the text variable.
        If the file filename exist it should overwrite the content
        of the file, but if filename does not exist it should create 
        the file and write the string to the file."""
    with open(filename,"w") as f:
        return(f.write(text))
    
def append_write(filename="",text=""):
    """Append text to the end of filename. if filename does not exist
    create file then append text"""
    with open(filename,"a",encoding="utf-8") as f:
        return(f.write(text))
    
def create_file(filename=""):
    with open(filename,"x") as f:
        return(f)
    
def to_json_string(obj):
    return(json.dumps(obj))

def from_json_string(my_str):
    return(json.loads(my_str))

def save_to_json_file(my_object,filename):
    with open(filename, "w") as f:
        our_file = json.dumps(my_object)
        return(f.write(our_file))

def load_from_json_file(filename):
    with open(filename,"r") as f:
        return json.loads(f.read())
    
def class_to_json(obj):
    return(obj.__dict__)

#
class Student:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        return self.__dict__

#
class Student:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self,attrs=None):
        if type(attrs) == list and (all(type(elem) == str for elem in attrs)):
            return{k:getattr(self,k) for k in attrs if hasattr(self,k)}
        return self.__dict__
    def reload_from_json(self,json):
        for k,v in json.items():
            setattr(self,k,v)

m1 = Student("mike","jim",43)
m2 = Student("nora","davies",21)
m_1 = m1.to_json()
m_2 = m2.to_json(["first_name","age"])
m_3 = m2.to_json(["middle_name","age"])
print(m_1)
print(m_2)
print(m_3)


def append_after(filename="", search_string="", new_string=""):
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
                with open(filename, "w") as a:
                    return a.write(text)

print(append_after("index.txt", "Python", "\"C is fun!\"\n"))