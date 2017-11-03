def draw_stars(arr):
	star = '*'
	for i in arr:
		if isinstance(i, str):
			print (len(i) * i[0]).lower()
			
		else:
			print star * i
draw_stars([1,'Tom',5,'Brady',9])
	


	
