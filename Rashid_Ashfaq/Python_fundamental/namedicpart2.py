users ={
'Student':[
	{'first_name':'Michael','last_name':'Jordan'},
	{'first_name': 'John', 'last_name': 'Rosales'},
	{'first_name': 'MArk', 'last_name': 'Guillen'},
	{'first_name': 'KB', 'last_name': 'Tonel'}
	],
'Instructor':[
	{'first_name': 'Michael','last_name':'Choi'},
	{'first_name': 'Martin', 'last_name':'Puryear'}
]
}
def userdisply():
	studentcount =0
	Instructorcount = 0
	print "Students"
	for key in users['Student']:
		student_length = len(key['first_name'])+ len(key['last_name'])
		studentcount= studentcount+1
		print studentcount , "-", key['first_name'],key['last_name'] ,"-" , student_length
	print "Instructor"
	for key1 in users['Instructor']:
		Instructor_length =len(key1['first_name']) + len(key1['last_name'])
		Instructorcount= Instructorcount+1
		print Instructorcount , "-" , key1['first_name'],key1['last_name'] ,"-", Instructor_length

userdisply()