class Person:
    """This is our parent class."""
    def __init__(self,name,age,ID):
        self.name = name
        self.age = age
        self.id = ID
    def show(self):
        print(f"my name is {self.name}")


class Employee(Person):
    """This subclass should provide us with basic information about the employee called Grey."""
    def __init__(self, name, age, ID,position):
         super().__init__(name, age, ID)
         self.position = position
         print("Initializing Employee...")
    def set_age(self):
        print(f"I am {self.age} years old")
 
    def add_position(self):
        print(f"my position is {self.position}")

    def get_Id(self):
        print(f"my staff ID is {self.id}")

    def setName(self):
        print(f"My name is {self.name}")


class Staff(Person):
    """This subclass should give basic information about a staff called Mellisa."""
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age, ID)
        self.salary = salary
        print("Intializing Staff...")

    def staffName(self):
        print(f"my name is {self.name}")

    def staff_age(self):
        print(f"I am {self.age} years old")

    def staff_Id(self):
        print(f"my staff ID is {self.id}")

    def staffSalary(self):
        print(f"my monthly salary is {self.salary}")


p = Person("DAVID", 23, 4)
p.show()
c = Employee("Grey",30,10,"HR")
c.add_position()
c.get_Id()
c.set_age()
c.setName()
f = Staff("Mellissa", 25, 3, "$2000")
f.staffSalary()
f.staff_Id()
f.staffName()
f.staff_age()

Person.__doc__
Employee.__doc__
Staff.__doc__

print(int('0x0ffff', base=0))
