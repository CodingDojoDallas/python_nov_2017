# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# def names():
# for key in students:
# 	print key['first_name'],key['last_name']
# names()


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names2():
	#key is Students and Instructors
	for key in users:
		count = 0
		print key
		#key1 is first_name and last_name
		for key1 in users[key]:
			count  +=1
			#print key1['first_name'],key1['last_name']
			print "{} - {} {} - {}".format(count,key1['first_name'],key1['last_name'],len(key1['first_name']+key1['last_name']))
names2()