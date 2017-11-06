def drawStars(a, var):
    b = []

    for i in a:
        i = i * var
        b.append (i)
    return b

a = [4, 6, 1, 3, 5, 7, 25]
for i in drawStars(a,"*"):
    print i
