def filter(a):
	if type(a)==list:
		if len(a)>=10:
			print "Big list!"
		else:
			print "Short list."

	
	elif type(a)==int:
		if a>=100:
			print "That's a big number!"
		else:
			print "That's a small number"
	
	elif type(a)==str:
		if len(a)>=50:
			print "Long sentence."
		else:
			print "Short sentence."
lL=[4,34,22,68,9,13,3,5,7,9,2,12,45,923]
filter(lL)
spL = ['name','address','phone number','social security number']
filter(spL)
