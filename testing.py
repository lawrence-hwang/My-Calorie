## UNIT TESTS

import unittest
import classes

class test_ingredients(unittest.TestCase):
    def test_create_class_successfully(self):
        bread = classes.ingredient("bread", 90, 5, 100, 0)
        self.assertEqual("bread",bread.get_name())

if __name__ == '__main__': 
    unittest.main() 
