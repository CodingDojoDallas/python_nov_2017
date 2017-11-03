'''Names'''

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#Part 1
def printName(dict):
    for x in students:
        print x['first_name'], x['last_name']
print "\nPart 1"
printName(students)

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

def printDict(dict):
    for role in dict:
        print role
        count = 0
        for x in dict[role]:
            print "{} - {} {} - {}".format(
                dict[role].index(x) + 1,
                x['first_name'].upper(),
                x['last_name'].upper(),
                len(x['first_name']) + len(x['last_name'])
            )

print "\nPart 2"
printDict(users)
