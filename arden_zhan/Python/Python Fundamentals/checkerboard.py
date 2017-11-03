'''Checkerboard'''

size = 8

evenrow = "* " * (size/2)
oddrow = " *" * (size/2)

for row in range(size):
    if row % 2 == 0: print evenrow
    else: print oddrow