# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for i in students:
#     print i['first_name'] +" "+ i['last_name']
#

#def print_dictionary_values(students):
    #    print students

#print_dictionary_values(students)

print "------"


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
def all(ppl):
    for x in(ppl):
        counter = 0
        print x
        for name in ppl[x]:# remember to carry the variable when needed
            counter += 1
            first_name = name['first_name']#make sure to call the variable ie *name*
            last_name = name['last_name']
            length = len(first_name)+len(last_name)
            print '{}-{} {}-{}'.format(counter , first_name, last_name, length)

all(users)
