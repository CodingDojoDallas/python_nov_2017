# Foo and Bar
# print all prime (foo) numbers and all perfect squares (bar)
# between 100 and 100,000

min = 100
max = 1000
notPrime = []
isPrime = []
isSquare = []

#start perfect square finder at min's sqrt
z = int(min**(0.5))
while z*z <= max:
    isSquare.append(z*z)
    z += 1

#sieve of Eratosthenes for primes
for x in range(2, max+1):
    if x not in notPrime:
        for y in range(x*x, max+1, x):
            notPrime.append(y)
        isPrime.append(x)

for i in range(min, max+1):
    if i in isPrime: print i, "foo"
    elif i in isSquare: print i, "bar"
    else: print i, "foobar"