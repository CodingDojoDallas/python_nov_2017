# function input
the_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]


def makingtupes(yup):
	newlist=[]
	for x,y in yup.iteritems():
		newlist.append((x,y))
	print newlist
makingtupes(the_dict)