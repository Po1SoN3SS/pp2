# # Python RegEx exercises
import re

# 1. Write a Python program that matches a string that has an `'a'` followed by zero or more `'b'`'s.
def a_more_b(string: str):
    pattern = r"ab*"
    match = re.fullmatch(pattern, string)
    return (match is not None)


print(a_more_b(input("String with a and zero or more b: ")))


# 2. Write a Python program that matches a string that has an `'a'` followed by two to three `'b'`.
def a_two_three_b(string: str):
    pattern = r"ab{2,3}"
    match = re.fullmatch(pattern, string)
    return (match is not None)

print(a_two_three_b(input("String with a and two or three b: ")))


# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.
def sequence_of_lowercase(string: str):
    pattern = r"^[a-z](?:_[a-z])*$"
    match = re.findall(pattern, string)
    return "".join(match)

print(sequence_of_lowercase(input("String with lowercase letters joined with underscore: ")))


# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def sequence_of_mixedcase(string: str):
    pattern = r"[A-Z][a-z]+"
    match = re.findall(pattern, string)
    return "".join(match)


print(sequence_of_mixedcase(input("String with uppercase letter followed by lowercase letters: ")))


# 5. Write a Python program that matches a string that has an `'a'` followed by anything, ending in `'b'`.
def a_anything_b(string: str):
    pattern = r"a.*b"
    match = re.match(pattern, string)
    return (match is not None)


print(a_anything_b(input("String that has \"a\" followed by anything, ending in b: ")))


# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replace_to_colon(string: str):
    pattern = r"[ ,.]"
    return re.sub(pattern, ":",string)


print(replace_to_colon(input("String where space, comma or dot will be replaced with a colon: ")))


# 7. Write a python program to convert snake case string to camel case string.
def snake_to_camel(string: str):
    result = [x.capitalize() for x in string.split("_")]
    return "".join(result)


print(snake_to_camel(input("String in snake case that will be converted to camel case: ")))


# 8. Write a Python program to split a string at uppercase letters.
def split_at_uppercase(string: str):
    pattern = r"[A-Z]"
    result = re.split(pattern, string)
    return result


print(split_at_uppercase(input("String that will be splitted at uppercase letters: ")))


# 9. Write a Python program to insert spaces between words starting with capital letters.
def insert_space(string: str):
    pattern = r"(\B[A-Z])"
    second_pattern = r" \1"
    result = re.sub(pattern, second_pattern, string)
    return result


print(insert_space(input("String where capital letters -> space and capital letters: ")))


# 10. Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(string: str):
    pattern = r"([A-Z]+)"
    second_pattern = r"_\1"
    result = re.sub(pattern, second_pattern, string)
    return result.lower()

print(camel_to_snake(input("String in came case that will be converted to snake case: ")))