from ipaddress import collapse_addresses


name = input("Hello, what is your name?")
print("Thanks {}, I will now convert your weight for you.".format(name.title()))
weight = float(input("What is your weight in pounds or kilograms:"))
unit = input("(K)g or (L)bs:")

# format vs rounding
if unit.capitalize() == "K":
    weight = (weight * 2.205)
    print("Your weight is {:.0f} lbs.".format(weight) )
    # print("Your weight is " + str(round(weight, 0)) + "lbs")
else:
    weight = (weight / 2.205)
    print("Your weight is {:.1f}kg ".format(weight))
    # print("Your weight is " + str(round(weight, 1)) + "kg")
