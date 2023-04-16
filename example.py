class Players:
        """This should collect basic information about a player."""

        perfect_foot = "left"       
        def __init__(self,name,age):
                """The name of the player"""
                self.var = name
                self.var1 = age
                print("FULL NAME: {}".format(self.var))
        def player_age(self):
                """player's age."""
                print("AGE: {:d}".format(self.var1))

        @classmethod
        def footter(cls):
                """Displays the perfect foot of the player"""
                print("{} is a {} footer".format(cls.var,cls.perfect_foot))
        
       

d = Players.footter("Lionel Messi")
print(d)


                