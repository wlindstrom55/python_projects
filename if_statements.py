temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else: # else statements runs if none of the others are true
    print("It's cold")
print("Done")
# if code is not indented, will always be executed.
# note: you couldn't use a single quote in this str because of the "It's"
# : is basically the bracket for a statement in Py. Denotes code block. block ends when code is no longer indented.
# elif stands for else if. like an else statement nested in an if statement.
# we can have as many conditions as we want.
