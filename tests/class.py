#!/usr/bin/python3

import unittest

class Test_for_Uppercase(unittest.TestCase):
    def test_upper(self):
        self.assertTrue("DAVID".isupper())
        self.assertFalse("nsk".isupper())

    def test_string(self):
        self.assertEqual("a"*4,"aaaa")

if __name__ == '__main__':
    unittest.main()
