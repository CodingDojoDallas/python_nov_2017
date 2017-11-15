def cointoss():
    counthead = 0
    counttail = 0  
    for i in range(1,5001):
        import random
        flip = random.randint(0,1)
        if flip == 0:
            counthead += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head!... Got " + str(counthead) + " head (s) so far and " + str(counttail) + " tail (s) so far"
        else:
            counttail += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail!... Got " + str(counthead) + " head (s) so far and " + str(counttail) + " tail (s) so far"
    total=counthead+counttail
    avg = 100*float(counthead)/float(total)
    print "You made {} attempts and {}% came up heads!".format(total, avg)
 
cointoss()