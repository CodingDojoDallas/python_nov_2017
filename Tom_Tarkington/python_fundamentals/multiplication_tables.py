def mult_tables():
    columns = 20
    rows = 50
    spaces = (len(str(columns*rows))+2)
    
    for y in range(rows+1):
        if y == 0:
            output = "x" + " "*(spaces-1)
        else:
            output = str(y) + " "*(spaces-len(str(y)))
            
        for count in range(1, columns+1):
            if y != 0:
                count*=y
            output+=str(count) + " "*(spaces-len(str(count)))
        print output
    
mult_tables()