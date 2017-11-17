students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]



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

def list_students(arr):
    for data in students:
        print data['first_name'], data['last_name']


def list_users(users):

    for i in users:
        counter = 0
        print i
        for person in users[i]:
            counter += 1

            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length_name = len(first_name) + len(last_name)
            print "{}-{} {}-{}".format(counter, first_name, last_name, length_name)


list_students(students)
list_users(users)
