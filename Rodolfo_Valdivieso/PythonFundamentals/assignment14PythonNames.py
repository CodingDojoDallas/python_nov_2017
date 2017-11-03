#Assignment 14 Python - Names
#Printing Values from a Dictionary
#Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print "Part1:"
print "------"

def names(dictionary):
	names=""
	for each in dictionary:
		for keys in each:
			names = names + each[keys] + " "
		print names
		names =""

names(students)

#Part 2
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

print "Part2:"
print "------"
def part2(dictionary2):
	
	for keys in dictionary2:
		count = 1
		print keys
		for i in dictionary2[keys]:
			print count,"-", i['first_name'] , " " , i['last_name'], "-", (len(i['first_name'])+len(i['last_name']))
			count=count+1

part2(users)