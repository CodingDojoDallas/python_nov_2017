Biodata ={"name": "Rashid","age": 30,"countofBirth": "Pakistan","language": "Python"}
def display(dictionaries):
	print "my name is ", Biodata["name"]
	print "my age is"  , Biodata["age"]
	print "my country of birth is", Biodata["countofBirth"]
	print "my favorite language is ", Biodata["language"]
	print "..........................................\n"
	print "All Value in Dictionary =" , Biodata.values()
	print "..........................................\n"
display(Biodata)

# print key and value
def value():
    for key,value in Biodata.items():
        print(key,value)

value()


