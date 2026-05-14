class RomanNumber:
    """
    A class representing a Roman numeral that can be initialized with either a Roman numeral string or an integer.
    """

    _roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    _decimal_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    _roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    def __init__(self, value):
        """
        Initialize the RomanNumber object with either a Roman numeral string or an integer.
        Args:
            value (str/int): Roman numeral string or integer in the range 1-3999
        """
        if isinstance(value, str):
            if self.is_roman(value):
                self.rom_value = value
                self.int_value = self._to_decimal(value)
            else:
                print("ошибка")
                self.rom_value = None
                self.int_value = None
        elif isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self._to_roman(value)
            else:
                print("ошибка")
                self.rom_value = None
                self.int_value = None
        else:
            print("ошибка")
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        Return the decimal (integer) equivalent of the Roman number.
        Returns:
            int/None: Integer value, or None if invalid
        """
        return self.int_value

    def roman_number(self):
        """
        Return the Roman numeral string equivalent of the decimal number.
        Returns:
            str/None: Roman numeral string, or None if invalid
        """
        return self.rom_value

    @staticmethod
    def is_roman(val):
        """
        Check if a string is a valid Roman numeral.
        Args:
            val (str): String to validate
        Returns:
            bool: True if the string is a valid Roman numeral, False otherwise
        """
        if not isinstance(val, str) or len(val) == 0:
            return False

        allowed = set('IVXLCDM')
        if not all(ch in allowed for ch in val):
            return False

        for sym in ['V', 'L', 'D']:
            if sym * 2 in val:
                return False

        for sym in ['I', 'X', 'C', 'M']:
            if sym * 4 in val:
                return False

        invalid_patterns = [
            'VX', 'VL', 'VC', 'VD', 'VM',
            'IL', 'IC', 'ID', 'IM',
            'XD', 'XM',
            'LC', 'LM',
            'DM'
        ]

        for ptrn in invalid_patterns:
            if ptrn in val:
                return False

        subtractive = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for combo in subtractive:
            if val.count(combo) > 1:
                return False

        roman_vals = RomanNumber._roman_values
        prev_val = float('inf')
        pos = 0
        length = len(val)

        while pos < length:
            if pos + 1 < length and roman_vals[val[pos]] < roman_vals[val[pos + 1]]:
                cur_val = roman_vals[val[pos + 1]] - roman_vals[val[pos]]
                if roman_vals[val[pos + 1]] > 10 * roman_vals[val[pos]]:
                    return False
                pos += 2
            else:
                cur_val = roman_vals[val[pos]]
                pos += 1

            if cur_val > prev_val:
                return False

            prev_val = cur_val

        return True

    @staticmethod
    def is_int(val):
        """
        Check if an integer is valid for Roman numeral representation.
        Args:
            val (int): Integer to validate
        Returns:
            bool: True if integer is in the range 1-3999, False otherwise
        """
        if not isinstance(val, int):
            return False
        if val < 1 or val > 3999:
            return False
        return True

    def _to_decimal(self, roman):
        """
        Convert a Roman numeral string to a decimal integer.
        Args:
            roman (str): Roman numeral string
        Returns:
            int: Integer value
        """
        total = 0
        prev_val = 0

        for ch in reversed(roman):
            cur_val = self._roman_values[ch]
            if cur_val < prev_val:
                total -= cur_val
            else:
                total += cur_val
            prev_val = cur_val

        return total

    def _to_roman(self, decimal):
        """
        Convert a decimal integer to a Roman numeral string.
        Args:
            decimal (int): Integer in the range 1-3999
        Returns:
            str: Roman numeral string
        """
        result = ""
        num = decimal
        for idx in range(len(self._decimal_values)):
            while num >= self._decimal_values[idx]:
                result += self._roman_symbols[idx]
                num -= self._decimal_values[idx]
        return result

    def __str__(self):
        """
        Return the Roman numeral string representation (or "None" if invalid).
        Returns:
            str: Roman numeral string or "None"
        """
        if self.rom_value is None:
            return "None"
        return self.rom_value

    def __repr__(self):
        """
        Return the formal representation for debugging.
        Returns:
            str: Formal string representation
        """
        if self.rom_value is None:
            return "RomanNumber(None)"
        return f"{self.rom_value}"

    def __add__(self, other):
        """
        Add two RomanNumber objects.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object as the sum, or invalid RomanNumber if error
        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                result = self.int_value + other.int_value
                if self.is_int(result):
                    return RomanNumber(result)
                else:
                    print("ошибка")
                    return RomanNumber(None)
        print("ошибка")
        return RomanNumber(None)

    def __sub__(self, other):
        """
        Subtract one RomanNumber object from another.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object as the difference, or invalid RomanNumber if error
        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                result = self.int_value - other.int_value
                if result < 1:
                    print("ошибка")
                    return RomanNumber(None)
                if self.is_int(result):
                    return RomanNumber(result)
                else:
                    print("ошибка")
                    return RomanNumber(None)
        print("ошибка")
        return RomanNumber(None)

    def __mul__(self, other):
        """
        Multiply two RomanNumber objects.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object as the product, or invalid RomanNumber if error
        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                result = self.int_value * other.int_value
                if result > 3999:
                    print("ошибка")
                    return RomanNumber(None)
                if self.is_int(result):
                    return RomanNumber(result)
                else:
                    print("ошибка")
                    return RomanNumber(None)
        print("ошибка")
        return RomanNumber(None)

    def __truediv__(self, other):
        """
        Divide one RomanNumber object by another using integer division.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object as the quotient, or invalid RomanNumber if error
        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                if other.int_value == 0:
                    print("ошибка")
                    return RomanNumber(None)
                result = self.int_value // other.int_value
                if result == 0:
                    print("ошибка")
                    return RomanNumber(None)
                if self.is_int(result):
                    return RomanNumber(result)
                else:
                    print("ошибка")
                    return RomanNumber(None)
        print("ошибка")
        return RomanNumber(None)

    def __floordiv__(self, other):
        """
        Floor divide one RomanNumber object by another.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object as the quotient, or invalid RomanNumber if error
        """
        return self.__truediv__(other)

    def __mod__(self, other):
        """
        Modulo of two RomanNumber objects.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object with the remainder, or invalid RomanNumber if error
        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                if other.int_value == 0:
                    print("ошибка")
                    return RomanNumber(None)
                result = self.int_value % other.int_value
                if result == 0:
                    print("ошибка")
                    return RomanNumber(None)
                if self.is_int(result):
                    return RomanNumber(result)
                else:
                    print("ошибка")
                    return RomanNumber(None)
        print("ошибка")
        return RomanNumber(None)

    def __pow__(self, other):
        """
        Raise the RomanNumber to the power of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: New RomanNumber object as the power, or invalid RomanNumber if error
        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                result = self.int_value ** other.int_value
                if result > 3999:
                    print("ошибка")
                    return RomanNumber(None)
                if self.is_int(result):
                    return RomanNumber(result)
                else:
                    print("ошибка")
                    return RomanNumber(None)
        print("ошибка")
        return RomanNumber(None)

    def __iadd__(self, other):
        """
        In-place addition of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: Self after addition
        """
        result = self.__add__(other)
        if result.int_value is not None:
            self.int_value = result.int_value
            self.rom_value = result.rom_value
        else:
            self.int_value = None
            self.rom_value = None
        return self

    def __isub__(self, other):
        """
        In-place subtraction of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: Self after subtraction
        """
        result = self.__sub__(other)
        if result.int_value is not None:
            self.int_value = result.int_value
            self.rom_value = result.rom_value
        else:
            self.int_value = None
            self.rom_value = None
        return self

    def __imul__(self, other):
        """
        In-place multiplication of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: Self after multiplication
        """
        result = self.__mul__(other)
        if result.int_value is not None:
            self.int_value = result.int_value
            self.rom_value = result.rom_value
        else:
            self.int_value = None
            self.rom_value = None
        return self

    def __itruediv__(self, other):
        """
        In-place division of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: Self after division
        """
        result = self.__truediv__(other)
        if result.int_value is not None:
            self.int_value = result.int_value
            self.rom_value = result.rom_value
        else:
            self.int_value = None
            self.rom_value = None
        return self

    def __ifloordiv__(self, other):
        """
        In-place floor division of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: Self after floor division
        """
        return self.__itruediv__(other)

    def __imod__(self, other):
        """
        In-place modulo of another RomanNumber.
        Args:
            other (RomanNumber): Another RomanNumber instance
        Returns:
            RomanNumber: Self after modulo
        """
        result = self.__mod__(other)
        if result.int_value is not None:
            self.int_value = result.int_value
            self.rom_value = result.rom_value
        else:
            self.int_value = None
            self.rom_value = None
        return self




a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
print(f / RomanNumber('II') )
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)
