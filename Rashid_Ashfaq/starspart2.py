def draw_stars(arr):
	for i in arr:
		if isinstance(i ,str):
			mystring= len(i)
			print i[0].lower()* mystring
		else:
			print "*" * i

x =[4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
draw_stars(x)