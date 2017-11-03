'''Stars'''
'''Part 1'''
# takes list of numbers and prints out *

def draw_stars(input):
    for i in range(len(input)):
        if type(input[i]) is str: 
            print (input[i][0]).lower() * len(input[i])
        else: print "*" * input[i]

x = [4, 6, 1, 3, 5, 7, 25]
print "Part 1"
draw_stars(x)

'''Part 2'''
# allow list containing integers and strings to be passed
# when string, display first letter of string instead. can use .lower()

print ""
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print "Part 2"
draw_stars(x)
