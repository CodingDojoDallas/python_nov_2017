def draw_stars(arr):
	stars = "*"
	for x in arr:
		if isinstance(x,str):
			print (x[0] * len(x)).lower()
		else:
			print x * stars
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])