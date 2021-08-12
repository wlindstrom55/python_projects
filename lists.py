# primitives are numbers (ints and floats), booleans, and strings
# complex types (Lists,
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
# we can also get single elements:
print(names [0])
# in python we can also use negative index**************
print(names[-1]) # represents last element in list
print(names[-2]) # represents 2nd to last
names[0] = "Jon" # changes the value of element
# range of values:
print(names[0:3]) # returns 0,1,2. BUT NOT 3. Returns a new list, doesn't modify old.

# List Methods: (lists have methods)
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # adds a 6 at the end
numbers.insert(0, -1) # you can use cmd-p to see what args are required for a method. useful af
numbers.remove(3) # removes 3
numbers.clear() # this method doesn't expect values, but instead clears the list

print(1 in numbers) # checks to see if 1 is in the numbers list. returns a boolean value.
print(len(numbers)) # len returns the # of total elements in a list.