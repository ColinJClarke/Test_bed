# Python program showing how to
# multiple input using split
  
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()
  
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()
  
# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print()
  
# note the 3 ''' creaate a multiple line comment
''' taking multiple inputs at a time 
and type casting using list() function '''
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)

# note the seperator - input("Enter multiple value: ").split(",")]

''' Python program showing
how to take multiple input items
using List comprehension '''
  
 # taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()
  
# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
print()
scores= [x,y,z]
total=sum(scores)
print()
print('Total score: ' + str(total))
  
# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()
  
# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)




