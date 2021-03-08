
import unittest
import leapyear
class leapyear1(unittest.TestCase):
    def test_leapyear(self):
        #take year from user
        print("enter your year.")
        input_year = int(input())
        result = leapyear.leapyear(input_year)
        if(input_year % 4 == 0 and input_year % 100 == 0 and input_year % 400 == 0):
            self.assertEqual(result, "Leap year")
        else:
            self.assertEqual(result, input_year)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(leapyear1('test_leapyear'))

    unittest.TextTestRunner().run(suite)