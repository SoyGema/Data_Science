
#-----------------------------------------------#
import unittest
import Loops


class MyTestCase(unittest.TestCase):
    def test_should_return_sum_array_when_input_is_array(self):
        self.assertEqual(3, Loops.sum_array([1,1,1]))


#-----------------------------------------------#



class MyTestCase(unittest.TestCase):
    def test_should_return_factorial_of_number(self):
        self.assertEqual(6, Loops.factorial(3))



#-----------------------------------------------#

class MyTestCase(unittest.TestCase):
    def test_should_return_factorial_of_number(self):
        self.assertEqual([0,1,1,2,3,5], Loops.fibonacci(5))

class MyTestCase(unittest.TestCase):
    def test_should_return_factorial_of_number(self):
        self.assertEqual([0], Loops.fibonacci(0))

if __name__ == '__main__':
    unittest.main()
