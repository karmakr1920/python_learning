# Roman numeral to integer mapping
def romanToInt(s):
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Result variable to store the final integer value
    result = 0
    # Iterate through the string (up to the second last character)
    for i in range(len(s) - 1):
        # If the current character's value is less than the next one,
        # we subtract its value
        if roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
            result -= roman_to_int_map[s[i]]
        else:
            result += roman_to_int_map[s[i]]
    
    # Add the value of the last character
    result += roman_to_int_map[s[-1]]
    
    return result
print(romanToInt('MIV'))