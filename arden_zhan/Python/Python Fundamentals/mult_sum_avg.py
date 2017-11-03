'''
Multiples, Sum, Average
'''

#Multiples
#Part 1 - Write code that prints all the odd numbers from 1 to 1000. for loop, no list
x = 1
while x <= 100:
    if x % 2 == 1:
        print x
    x += 2


print""
#Part 2 - multiples of 5 from 5 to 100
x = 5
while x <= 100:
    if x % 5 == 0:
        print x
    x += 5


print ""
#Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in a:
    sum += val
print sum


print ""
#Average List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in a:
    sum += val
avg = sum / len(a)
print avg

