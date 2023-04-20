import unittest

from models.Rectangle import Rectangle

class TestmyModule(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(10,3)
        self.assertEqual(r1.id,1)
        r2 = Rectangle(5,21,6)
        self.assertEqual(r2.id,2)
        r3 = Rectangle(12,4,7,2,12)
        self.assertEqual(r3.id,12)

if __name__ == "__main__":
    unittest.main()
