import random

def coinToss(num):
    attempt = 1
    heads = 0
    tails = 0
    results = ""
    counter = ""

    for x in range(1,num):
        toss = random.randint(0,1)
        if toss == 1:
            heads += 1
            result = "heads"
            print "attempt #", count, ": Throwing coin, it's a ", result, "got", heads, "heads for far and ", tails, "so far"

        else:
            tails +=1
            result = "tails"
            print "attempt #", count, ": Throwing coin, it's a ", result, "got", heads, "heads for far and ", tails, "so far"
        count +=1

coinToss(5001)
