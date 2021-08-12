# write a weight converter program
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

# have to make sure to be convertying types correctly. You cant concat a str to a float, and weight
# must be converted to int or float for 'converted' var operation to occur.


