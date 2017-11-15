



#def drawStars(x):

x=[4,6,1,3]

for i in range(0,len(x)):
	y=x[i]
	star=''
	for n in range(0,y):
		star+='*'
	print star



#def draw_Stars(x):

x=[4, 'tom', 1, 'michael']

for i in range(0,len(x)):
	y=x[i]
	if type(y)==str:
		#do something here
		str1=''
		for n in range(0,len(y)):
			str1+=(y[0])
	else:
		star=''
		for n in range(0,y):
			star+='*'
		print star



