import unittest
from  models.base import Base
Base = __import__("base").Base

class Test_Base(unittest.TestCase):
    def increment_id(self):

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id,b2.id -1,"i'm i correct?")
        
if __name__ == "__main__":
    unittest.main()
