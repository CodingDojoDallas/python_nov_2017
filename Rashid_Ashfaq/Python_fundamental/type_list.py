l = ['magical unicorns',19,'hello',98.98,'world']
sum=0
string=''
data = [False,False]
for i in l:
    if isinstance(i,float) or isinstance(i,int):
        sum+=i
        data[0]=True
    else:
        string+= i + ' '
        data[1]=True

if all(data):print "The array you entered is of mixed String",(string.strip(),sum)
elif data[1]:print "The array you entered is of string =",string.strip()
elif data[0]:print "The array you entered is of Sum =/n",sum
