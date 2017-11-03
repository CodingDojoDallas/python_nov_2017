'''Scores and Grades'''
# generates ten scores between 60 and 100. Each time score generated, displays what grade is for particular score.
'''
Grade Table
Score: 60-79; Grade - D
Score: 70-79; Grade - C
Score: 80-89; Grade - B
Score: 90-100; Grade - A
'''

# import random
# #random_num = random.random()
# #random function returns float - 0.0 <= random_num < 1.0
# random_num = random.randint(60, 100)
import random
def scoreGrade(quantity, min, max):
    for x in range(quantity):
        random_num = random.randint(min, max)
        grade = ""
        if random_num >= 90: grade += "A"
        elif random_num >= 80: grade += "B"
        elif random_num >= 70: grade += "C"
        else: grade += "D"
        print "Score: {}; Your grade is {}".format(random_num, grade)

scoreGrade(10, 60, 100)
