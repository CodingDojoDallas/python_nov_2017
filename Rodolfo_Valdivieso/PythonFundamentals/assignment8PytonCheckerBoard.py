

#CheckerBoard Assignment

even_row = "* " * 4
odd_row =  " *" * 4

for x in range(1,9):
	if x % 2 == 0:
		print even_row
	else:
		print odd_row
