#List
#If the length of the list is greater than or equal to 10 print "Big list!"
#If the list has fewer than 10 values print "Short list."
variable = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
if isinstance(variable, list):
    if len(variable) >= 10:
         print "Big list!"
    else: 
        print "Short list." 
