weight = float(input("what is your weight:"))
unit = input("(K)g or (L)bs:")

# format vs rounding
if unit.capitalize() == "K":
    weight = (weight * 2.205)
    print("Your weight is {:.0f}lbs.".format(weight) )
    # print("Your weight is " + str(round(weight, 0)) + "lbs")
else:
    weight = (weight / 2.205)
    print("Your weight is {:.1f}kg ".format(weight))
    # print("Your weight is " + str(round(weight, 1)) + "kg")
