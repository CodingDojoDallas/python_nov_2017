'''Coin Tosses'''
# simulates tossing coin 5000 times. prints how many times heads/tails appears

'''
?? not sure why need float
round function converts floating point number into integer.
x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1
'''

import random
def toss(amount):
    heads = 0
    tails = 0
    
    for x in range(amount):
        if random.randint(0,1) == 0:
            state = "head"
            heads += 1
        else:
            state = "tail"
            tails += 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(
            x + 1, state, heads, tails 
        )

toss(50)
