def checkprime(num):
    isprime = True
    for idx in range(2,num-1):
        if num % idx == 0:
            isprime = False
    return(isprime)

def checksquare(num):
    issquare = False

    for idx in range(2, num):
        if idx**2 == num:
            issquare = True
    return(issquare)

for runner in range(100, 100001):
    if checkprime(runner):
        print str(runner) + " is Foo"
    elif checksquare(runner):
        print str(runner) + " is Bar"
    else:
        print str(runner) + " is FooBar"