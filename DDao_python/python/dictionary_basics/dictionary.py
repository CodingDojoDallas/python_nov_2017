dict = {"name": "Young", "age": "85", "country of birth": "USA", "favorite language": "Japanese"}

def dictionary():
	for keys, values in dict.iteritems():
		print 'My {} is {}'.format(keys, values)

