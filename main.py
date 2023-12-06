import unittest
from tp9 import Fraction

class FractionTest(unittest.TestCase) :
    
    def test_init_zeroDivision(self):
        self.assertRaises(ZeroDivisionError,Fraction,2,0)
    
    def test_init_random_fraction(self):
        fraction_random = Fraction(1,2)
        self.assertEqual(fraction_random.numerator,1,"Fraction(1,2) numerator must be equal to 1")
        self.assertEqual(fraction_random.denominator,2,"Fraction(1,2) denominator must be equal to 2")
    
    def test_2_negatives_number(self):
        fraction_negative_num_den = Fraction(-1,-2)
        fraction_negative_den = Fraction(1,-2)
        fraction_negative_num = Fraction(-1,2)
        self.assertEqual(str(fraction_negative_num_den),"1/2","For Fraction(-1,-2) the result must be equal to 1/2")
        self.assertEqual(str(fraction_negative_den),"-1/2","For Fraction(1,-2) the result must be equal to -1/2") 
        self.assertEqual(str(fraction_negative_num),"-1/2","For Fraction(-1,2) the result must be equal to -1/2")
    
    def test_fraction_simplified(self):
        fraction_to_simplified = Fraction(8,4)
        self.assertEqual(str(fraction_to_simplified),"2","Fraction(8,4) must be equal to 2")
    
    def test_str_fraction(self):
        fraction_str = Fraction(1,2)
        fraction_unit = Fraction(8,8)
        entier = Fraction(16,8)
        self.assertEqual(str(fraction_str),"1/2","The method __str__ of Fraction(1,2) must return string '1/2' ")
        self.assertEqual(str(fraction_unit),"1","The method __str__ of Fraction(8,8) must return '1' ")
        self.assertEqual(str(entier),"2","The method __str__ of Fraction(16,8) must return the string '2' ")
    
    def test_mixed_number(self):
        self.assertEqual(Fraction(5,3).as_mixed_number(),"1 + 2/3","Mixed number of Fraction(5,3) must take the form of '1 + 2/3' ")
        self.assertEqual(Fraction(5,4).as_mixed_number(),"1 + 1/4","Mixed number of Fraction(5,4) must take the form of '1 + 1/4' ")
        self.assertEqual(Fraction(9,2).as_mixed_number(),"4 + 1/2","Mixed number of Fraction(9,2) must take the form of '4 + 1/2' ")
        
    def test_addition(self):
        self.assertEqual(str(Fraction(2,3) + Fraction(1,3)),"1","Addition of Fraction(2,3) with Fraction(1,3) must be equal to 1")
        self.assertEqual(str(Fraction(3,3) + Fraction(2,3)),"5/3","Addition of Fraction(3,3) with Fraction(2,3) must be equal to 5/3")
    
    def test_substraction(self):
        self.assertEqual(str(Fraction(5,3) - Fraction(1,4)),"17/12","Substraction of Fraction(5,3) with Fraction(1,4) must be equal to 17/12")
        self.assertEqual(str(Fraction(8,6) - Fraction(1,5)),"17/15","Substraction of Fraction(8,6) with Fraction(1,5) must be equal to 17/15")
    
    def test_multiplication(self):
        self.assertEqual(str(Fraction(5,4) * Fraction(1,2)),"5/8","Multiplication of Fraction(8,6) with Fraction(1,5) must be equal to 5/8")
        self.assertEqual(str(Fraction(0) * Fraction(2,5)),"0","Multiplication of Fraction(0) with Fraction(2,5) must be equal to 0")
        self.assertEqual(str(Fraction(-1) * Fraction(9,2)),"-9/2","Multiplication of Fraction(-1) with Fraction(9,2) must be equal to -9/2")
    
    def test_division(self):
        self.assertEqual(str(Fraction(9,8)/Fraction(1,2)),"9/4","Division of Fraction(9,8) with Fraction(1,2) must be equal to 9/4")
    
    def test_equal(self):
        self.assertTrue(str(Fraction(2,4)) == str(Fraction(1,2)),"Simplified Fraction(2,4) equals Fraction(1,2)")

    def test_float(self):
        fraction_float=Fraction(1,2)
        self.assertTrue(isinstance(fraction_float.numerator/fraction_float.denominator,float))
    
    def test_lower_than(self):
        highest_fraction = Fraction(6,7)
        lowest_fraction = Fraction(5,7) 
        self.assertTrue(lowest_fraction.__lt__(highest_fraction),"Fraction(5,7) is strictly lower than Fraction(6,7)")
    
    def test_greater_than(self):
        highest_fraction = Fraction(6,7)
        lowest_fraction = Fraction(5,7) 
        self.assertTrue(highest_fraction.__gt__(lowest_fraction),"Fraction(6,7) is strictly greater than Fraction(5,7)")
    
    def test_opposite(self):
        fraction = Fraction(6,7)
        different_fraction = Fraction(5,7) 
        self.assertTrue(fraction.__ne__(different_fraction),"Fraction(6,7) is different than Fraction(5,7)")
    
    def test_lower_equals(self):
        fraction = Fraction(6,7)
        lowest_fraction = Fraction(5,7) 
        same_fraction = Fraction(12,14)
        self.assertTrue(lowest_fraction.__le__(fraction),"Fraction(5,7) is lower than Fraction(6,7)")
        self.assertTrue(fraction.__le__(same_fraction),"Fraction(6,7) is equal to Fraction(12,14)")
    
    def test_greater_equals(self):
        fraction = Fraction(3,8)
        highest_fraction = Fraction(7,9) 
        same_fraction = Fraction(6,16)
        self.assertTrue(highest_fraction.__ge__(fraction),"Fraction(7,9) is greater than Fraction(3,8)")
        self.assertTrue(fraction.__ge__(same_fraction),"Fraction(3,8) is equal to Fraction(6,16)")

    def test_is_zero(self):
        self.assertTrue(Fraction(0,12).is_zero(),"Fraction(0,12) is equal to zero")
        
    def test_is_integer(self):
        self.assertTrue(Fraction(4,2).is_integer(),"Fraction(4,2) is equal to 2 which is an integer")

    def test_is_proper(self):
        self.assertTrue(Fraction(-1,2),"Fraction(-1,2) is lower than 1")

    def test_is_unit(self):
        self.assertTrue(Fraction(3,12),"Fraction(3,12) is equal to Fraction(1,4) in its reduced form, the numerator is equal to 1")

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1,2).is_adjacent_to(Fraction(3,2)),"Fraction(1,2) is adjacent to Fraction(3,2)")


if "__name__" == "__main__":
    unittest.main()