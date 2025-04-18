import math
people = int(input("Enter the number of people that need pizza: "))
slices = float(input("Enter the number of slices per person that are needed: "))
total_slices = people * slices
pizzas = (people * slices / 8)
print ("The total number of slices that are needed is ", total_slices)
print (math.ceil(pizzas), 'pizzas are needed.  Each pizza has 8 slices.')