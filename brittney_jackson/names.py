#create a program that outputs all values

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in students:
	print i['first_name']+' '+i['last_name']

print '---------------'


#create a program that outputs all values + num of characters in each name

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


for i in users:
	print i
	num = 0
	for j in users[i]:
		num +=1
		print str(num)+' - '+j['first_name']+' '+ j['last_name']+' - '+str(len(j['first_name']+j['last_name']))
		











