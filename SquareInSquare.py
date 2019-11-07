# SquareInSquare.py
# author: Marcus Campbell
# date: 07/11/19
#
# Calculates the area of a square cut out shape

print("Welcome the the shape calculator.")

large_height = int(input("\nPlease enter the value for g "))
large_base = int(input("\nPlease enter the value for s "))

small_height = int(input("\nPlease enter the value for w "))
small_base = int(input("\nPlease enter the value for q "))

large_square = large_height * large_base
small_square = small_height * small_base
total_area = large_square - small_square

print("\nThe total area of the shape is", total_area)

input("\nPlease press enter to exit.")

'''
Assertion is that if:
s = 4, g = 2 then large = 8
and
q = 2, w = 1 then small = 2
then
total = 6
'''
