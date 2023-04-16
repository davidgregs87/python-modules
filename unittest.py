import unittest
import diy_modules

class TestModule(unittest.TestCase):

    def test_find_index(self):
        result = diy_modules.find_index(["math","biology","physics","science"], "biology")
        self.assertEqual(result, 1)
if __name__ == "__main__":
    unittest.main()


