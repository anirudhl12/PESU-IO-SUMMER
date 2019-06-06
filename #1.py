
#1. Write a Python program which accepts a sequence of comma-separated numbers
#from the user and generate a list and a tuple with those numbers.


sequence = input("Enter numbers separated by commas : \n")
a = []
a = sequence.split(",")
b = tuple(a)
print(' The list is, ',a)
print(' The tuple is, ',b)
