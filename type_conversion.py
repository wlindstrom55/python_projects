# 3 types of data in python
10
# numbers
"Mosh"
# strings
True
# booleans
birth_year = input("Enter your birth year: ")
# input returns a string. You can't subtract a String from an int, so you get a type error
# below you will see Pythons equivalent to casting in Java (int and str)
age = 2020 - int(birth_year)
print("You are " + str(age) + " years old.")

# built-in functions for converting values:
int()
float()
bool()
str()

# Python doesn't know how to concatenate different type values. So these are important.