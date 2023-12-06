# from fractionFinalimport Fraction
class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num is an integer with 0 as default value, and den is a non-zero integer with 1 as default value; both are immutable
        POST : If den is not zero, a new fraction is constructed with values equivalent to num/den.

        """
        self.__num = num
        self.__den = den
        if den == 0:
            raise ZeroDivisionError("Fraction cannot have a null denominator")

        # Simplify the fraction using GCD (Greatest Common Divisor) or GCPD in French
        denTemp = den
        pgcd = num
        while denTemp:
            pgcd, denTemp = denTemp, pgcd % denTemp
        if pgcd:
            self.__num = self.__num // pgcd
            self.__den = self.__den // pgcd
        if self.__den < 0:
            self.__den *= -1
            self.__num *= -1

    @property
    def numerator(self):
        return self.__num

    @numerator.setter
    def numerator(self, other):
        self.__num = other

    @property
    def denominator(self):
        return self.__den

    @denominator.setter
    def denominator(self, other):
        self.__den = other

        # simplification

    @property
    def fraction(self):
        return self.numerator / self.denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : Returns a textual representation of the reduced fraction
                Example: str(Fraction(1/3)) returns "1/3"
        """
        if self.numerator%self.denominator == 0:
            return str(int(self.numerator/self.denominator))
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None
        POST : None (Explanation of the method's functionality)
            Example: 5/3 = 1 + 2/3
        """
        integer = self.numerator // self.denominator
        remain = self.numerator % self.denominator
        return f"{integer} + {remain}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : other is an instance of class Fraction
        POST : self and other are unchanged, return a new object from class Fraction, value is the sum of self and other
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return Fraction(self.numerator + other.numerator, self.denominator)
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return Fraction(new_num_self + new_num_other, new_denom)
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during addition: {e}")
            return None

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is an instance of class Fraction
        POST : self and other are unchanged, return a new object from class Fraction, value is the difference of self and other
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return Fraction(self.numerator - other.numerator, self.denominator)
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return Fraction(new_num_self - new_num_other, new_denom)
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during subtraction: {e}")
            return None

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is an instance of class Fraction
        POST : self and other are unchanged, return a new object from class Fraction, value is the product of self and other
        """
        try:
            if isinstance(other, Fraction):
                return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during multiplication: {e}")
            return None

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is an instance of class Fraction
        POST : self and other are unchanged, return a new object from class Fraction, value is the division of self by other
        """
        try:
            if isinstance(other, Fraction):
                if other.numerator != 0:
                    return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
                else:
                    raise ZeroDivisionError("Other's numerator can't be zero")
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during division: {e}")
            return None

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other is an int
        POST : self and other are unchanged, return a new object from class Fraction, value is self raised to the power of other
        """
        try:
            if isinstance(other, int):
                return Fraction(self.numerator ** other, self.denominator ** other)
            else:
                raise TypeError("Other must be an int")
        except Exception as e:
            print(f"An error occurred during exponentiation: {e}")
            return None

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other is an instance of class Fraction
        POST : Returns True if self and other are equal fractions, returns False otherwise
        """
        try:
            if isinstance(other, Fraction):
                return self.numerator == other.numerator and self.denominator == other.denominator

            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return False

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None
        POST : Returns a float representing the decimal value of the fraction
        """
        try:
            return float(self.fraction)
        except Exception as e:
            print(f"An error occurred during conversion to float: {e}")
            return None

        # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    def __lt__(self, other):
        """Overloading of the < operator for fractions

        PRE : other is an instance of class Fraction
        POST : Returns True if self is less than other, False otherwise
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return self.numerator < other.numerator and self.denominator == other.denominator
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return new_num_self < new_num_other and new_denom == new_denom
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return False

    def __gt__(self, other):
        """Overloading of the > operator for fractions

        PRE : other is an instance of class Fraction
        POST : Returns True if self is greater than other, False otherwise
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return self.numerator > other.numerator and self.denominator == other.denominator
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return new_num_self > new_num_other and new_denom == new_denom
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return False

    def __ne__(self, other):
        """Overloading of the != operator for fractions

        PRE : other is an instance of class Fraction
        POST : Returns True if self is not equal to other, False otherwise
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return self.numerator != other.numerator and self.denominator == other.denominator
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return new_num_self != new_num_other and new_denom == new_denom
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return False

    def __le__(self, other):
        """Overloading of the <= operator for fractions

        PRE : other is an instance of class Fraction
        POST : Returns True if self is less than or equal to other, False otherwise
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return self.numerator <= other.numerator and self.denominator == other.denominator
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return new_num_self <= new_num_other and new_denom == new_denom
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return False

    def __ge__(self, other):
        """Overloading of the >= operator for fractions

        PRE : other is an instance of class Fraction
        POST : Returns True if self is greater than or equal to other, False otherwise
        """
        try:
            if isinstance(other, Fraction):
                if self.denominator == other.denominator:
                    return self.numerator >= other.numerator and self.denominator == other.denominator
                else:
                    new_denom = self.denominator * other.denominator
                    new_num_self = self.numerator * other.denominator
                    new_num_other = other.numerator * self.denominator
                    return new_num_self >= new_num_other and new_denom == new_denom
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return False

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None
        POST : Returns True if the fraction's value is 0, False otherwise
        """
        try:
            return self.numerator == 0
        except Exception as e:
            print(f"An error occurred during checking if the fraction is zero: {e}")
            return False

    def is_integer(self):
        """Check if a fraction is an integer

        PRE : None
        POST : Returns True if the fraction is an integer, False otherwise
        """
        try:
            return self.numerator%self.denominator == 0
        except Exception as e:
            print(f"An error occurred during checking if the fraction is an integer: {e}")
            return False

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None
        POST : Returns True if the absolute value of the fraction is less than 1, False otherwise
        """
        try:
            return abs(self.numerator/self.denominator) < 1
        except Exception as e:
            print(f"An error occurred during checking if the fraction is proper: {e}")
            return False

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None
        POST : Returns True if the fraction's numerator is 1 in its reduced form, False otherwise
        """
        try:
            return self.numerator == 1
        except Exception as e:
            print(f"An error occurred during checking if the fraction is a unit: {e}")
            return False

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference between them is a unit fraction

        PRE : other is an instance of class Fraction
        POST : Returns True if the difference between self and other is a unit fraction, returns False otherwise
        """
        try:
            if isinstance(other, Fraction):
                return abs(int(str(self.__sub__(other))))==1
            else:
                raise TypeError("Other must be an instance of class Fraction")
        except Exception as e:
            print(f"An error occurred during checking if the fractions are adjacent: {e}")
            return False

