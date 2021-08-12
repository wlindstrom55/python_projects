course = 'Python for Beginners'
print(course.upper())
# Strings are objects. Objects have capabilities (methods/functions).
# When a function is part of an object, we refer to that as a method.
# Upper method does not change original string, but INSTEAD returns a new string
print(course.find('y'))
# above will return 1, since the index of y in the string is 1. P is 0. find() looks for occurrences
print(course.replace('for', 4))
# this method replaces 'for' with a string containing 4. Replace method returns a new string also
# Strings in python and other languages are immutable, we cannot change them unless we create them
# There are times you wanna see if you String contains a character or series of em
print(course.find("Python"))
# in operator. Below we would see a boolean value returned.
print('Python' in course)