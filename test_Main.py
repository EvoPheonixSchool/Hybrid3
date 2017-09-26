#By: Sheldon McGrath

import unittest
import Main

class testMain(unittest.TestCase):
    def setUp(self):
        pass

    #testing add function
    def test_add(self):
        self.assertEqual(Main.add(2,2), 4)

    #testing subtract function
    def test_subtract(self):
        self.assertEqual(Main.subtract(2,2), 0)

    #testing divide function
    def test_divide(self):
        self.assertEqual(Main.divide(2,2), 1)

    #testing multiply  function
    def test_multiply(self):
        self.assertEqual(Main.multiply(2,2), 4)

if __name__ == '__main__':
    unittest.main()
