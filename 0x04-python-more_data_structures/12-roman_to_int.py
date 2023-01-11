#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    sum_num = 0
    temp = roman_string[0]
    for char in roman_string:
        if char in roman_numeral.keys():
            if roman_numeral[char] > roman_numeral[temp]:
                sum_num += (roman_numeral[char] - 2 * roman_numeral[temp])
                temp = char
                continue
            sum_num += roman_numeral[char]
            temp = char
        else:
            return 0

    return sum_num
