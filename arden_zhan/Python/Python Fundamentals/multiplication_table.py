'''Multiplication Table'''


for row in range(0, 12 + 1):
    
    if row == 0:
        result = "x"
    else:
        result = str(row)
    for y in range(1,13):
        if row == 0:
            row = 1
        product = str(y * row)
        result += "{}{}".format(" ", product)
    print result