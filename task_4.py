class RomanNumber:
    """
    Represents a Roman numeral and provides functionality to
    validate and convert it to its decimal (Arabic) equivalent.
    """

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, rom_value):
        """
        Initialize a new RomanNumber instance with the given Roman numeral string.
        If the string is not a valid Roman numeral, sets the value to None.

        Args:
            rom_value (str): The Roman numeral as a string.
        """
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print("ошибка")  # Consider changing to an exception for production
            self.rom_value = None

    def decimal_number(self):
        """
        Converts the Roman numeral represented by this instance to its decimal value.
        Returns None if the Roman numeral is invalid.

        Returns:
            int or None: The decimal (Arabic) value or None if the numeral is invalid.
        """
        if self.rom_value is None:
            return None

        total = 0
        prev_val = 0

        for ch in reversed(self.rom_value):
            cur_val = self.roman_values[ch]

            if cur_val < prev_val:
                total -= cur_val
            else:
                total += cur_val

            prev_val = cur_val

        return total

    @staticmethod
    def is_roman(val):
        """
        Checks whether a given string is a valid Roman numeral
        according to traditional rules.

        Args:
            val (str): The string to be checked.

        Returns:
            bool: True if the string represents a valid Roman numeral, False otherwise.
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

        roman_vals = RomanNumber.roman_values
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

    def __str__(self):
        """
        Returns the standard string representation of the Roman numeral.
        Returns 'None' if the value is not set or invalid.

        Returns:
            str: The Roman numeral as a string, or 'None'.
        """
        if self.rom_value is None:
            return "None"
        return self.rom_value

    def __repr__(self):
        """
        Returns a detailed string representation suitable for debugging.

        Returns:
            str: A representation indicating the Roman numeral or None.
        """
        if self.rom_value is None:
            return "None"
        return f"{self.rom_value}"



num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))
