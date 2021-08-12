numbers = range(5) # returns a range object 0-5, excluding 5.
# a range object can store a sequence of numbers
print(numbers) # this will only print the range arguments

# how do we print the numbers from a range? (enhanced?)for loop:
for number in numbers:
    print(number)

# you can have a third arg, which is the # of steps b/w elements in range.
# also, we don't really need to store the result in a separate var like numbers, since:
for numbers in range(5):
    print(number) # would do the same thing.