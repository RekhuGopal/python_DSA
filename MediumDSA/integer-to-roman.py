def intToRoman(num):
    # Define the mapping of decimal values to Roman numeral symbols
    mapping = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    roman_numeral = ''
    # Iterate through the mapping and construct the Roman numeral
    for value, symbol in mapping:
        while num >= value:
            roman_numeral += symbol
            num -= value

    return roman_numeral

# Test cases
print("Output for num = 3749:", intToRoman(3749))  # Output: "MMMDCCXLIX"
print("Output for num = 58:", intToRoman(58))      # Output: "LVIII"
print("Output for num = 1994:", intToRoman(1994))  # Output: "MCMXCIV"
