import random
def coin_toss(flips):
    head = 0
    tails = 0
    total_amnt = 0
    attempts = 1
    results = ""

    for i in range(flips):
        new_flip = random.randint(0,1)
        if new_flip == 1:
            head +=1
            results = "head"
            print "Attempt #", attempts, ": Throwing a coin...It's a ", results, "! Got ", head, "heads so far and", tails, "tails so far"
        else: 
            tails += 1
            results = "tail"
            print "Attempt #", attempts, ": Throwing a coin... It's a ", results, "! Got ", head, "heads so far and", tails, "tails so far"
            attempts += 1

coin_toss(5001)
