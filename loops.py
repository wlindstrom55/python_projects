# while loops
i = 1
while i <= 1_000: # we use underscores to make code more readable
    print(i * '*') # we can multiply a number and string together. Will repeat the string BASED on the # value
    i += 1
# prints numbers 1 - 5 as an example.

# for loops: (shorter and easier to understand)
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)
# this same code would be a bit longer in a while loop:
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1