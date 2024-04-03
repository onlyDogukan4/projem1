import unittest

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
    def simplify(self):
        y=self.denominator
        x=self.numerator
        while x>0:
            y,x=x,y%x
        self.denominator=self.denominator//y
        self.numerator=self.numerator//y
        return(self.numerator,self.denominator)
    
    def add(self,coords):
        numerator2,denominator2=coords
        a=numerator2
        b=denominator2

        y=self.denominator
        x=self.numerator
        while b>0:
            y,b=b,y%b
        lcm=self.denominator*denominator2//y
        if self.denominator!=denominator2:
            self.numerator,self.denominator=(lcm//self.denominator)*self.numerator,(lcm//self.denominator)*self.denominator
            numerator2,denominator2=(lcm//denominator2)*numerator2,(lcm//denominator2)*denominator2
            return(self.numerator+numerator2,lcm)
    def subtract(self, coords):
        numerator2,denominator2=coords
        a=numerator2
        b=denominator2

        y=self.denominator
        x=self.numerator
        while b>0:
            y,b=b,y%b
        lcm=self.denominator*denominator2//y
        if self.denominator!=denominator2:
            self.numerator,self.denominator=(lcm//self.denominator)*self.numerator,(lcm//self.denominator)*self.denominator
            numerator2,denominator2=(lcm//denominator2)*numerator2,(lcm//denominator2)*denominator2
            return(self.numerator-numerator2,lcm)

    def multiply(self, coords):
        numerator,denominator=coords
        numerator,denominator=numerator*self.numerator,denominator*self.denominator
        return(numerator,denominator)

    def divide(self, coords):
        denominator,numerator=coords
        numerator,denominator=numerator*self.numerator,denominator*self.denominator
        return(numerator,denominator)

class TestFractionAddition(unittest.TestCase):
    def test_addition(self):
        # Test case 1
        fraction1 = Fraction(1, 2)
        result = fraction1.add((1, 3))
        self.assertEqual(result, (5, 6))

        # Test case 2
        fraction2 = Fraction(3, 4)
        result = fraction2.add((2, 5))
        self.assertEqual(result, (23, 20))

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFractionAddition)

    # Create a test runner
    test_runner = unittest.TextTestRunner()

    # Run the tests
    test_runner.run(test_suite)
