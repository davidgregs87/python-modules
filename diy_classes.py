class TeamMember:
    """Retrieving infomation from a team. I'll be going about this using INHERITANCE in python"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Initialize TeamMember: {}".format(self.name))
    
    def info(self):
        """Basic team infomation about coach and players"""
        print('Name: {} Age: {}'.format(self.name,self.age))


class Coach:
    """Represent the Coach subclass"""
    def __init__(self,name,age,salary):
        TeamMember.__init__(self,name,age)
        self.salary=salary
        print('(Initialize Coach: {})'.format(self.name))

    def info(self):
        TeamMember.info(self)
        print('Salary: {:d}'.format(self.salary))

class Player:
    """Represent the player subclass"""
    def __init__(self,name,age,shirt_num):
        TeamMember.__init__(self,name,age)
        self.shirt_num=shirt_num
        print('(Initialize player: "{}"'.format(self.name))

    def info(self):
        TeamMember.info(self)
        print('Shirt number: {:d}'.format(self.shirt_num))

d = Coach("Mrs Mia Khalifa",32,45000)
f = Player("Davidgregs",45,7)

print()

members = [d,f]
for i in members:
    i.info()

    """THIS CODE IS TO DEMONSTRATE INHERITANCE IN OOP IN PYTHON."""
TeamMember.__doc__
TeamMember.info.__doc__
Coach.__doc__