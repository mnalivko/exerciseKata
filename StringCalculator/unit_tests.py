import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        #given
        num = ""
        calculator = StringCalculator()
        #when
        result = calculator.calculate(num)
        #then
        self.assertEqual(result, 0)

    def test_single_number(self):
        #given
        num = "5"
        calculator = StringCalculator()
        #when
        result = calculator.calculate(num)
        #then
        self.assertEqual(result, 5)
    
    def test_two_numbers_comma_delimited(self):
        # given
        num = "2,3"
        calculator = StringCalculator()
        # when
        result = calculator.calculate(num)
        # then
        self.assertEqual(result, 5)

    def test_two_numbers_newline_delimited(self):
        # given
        num = "2\n3"
        calculator = StringCalculator()
        # when
        result = calculator.calculate(num)
        # then
        self.assertEqual(result, 5)
    

if __name__ == '__main__':
    unittest.main()
