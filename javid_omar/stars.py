def draw_stars(arr):
	for element in arr:
		num=element
		line=""
		for i in range(num):
			line+="*"
		print line
x=[4,6,1,3,5,7,25]
draw_stars(x)

def draw_stars2(newarr):
	for element in newarr:
		line=""
		if type(element)==int:
			num=element
			for i in range(num):
				line+="*"
		if type(element)==str:
			char=element[0]
			char=char.lower()
			for i in range(len(element)):
				line+=char

		print line
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
