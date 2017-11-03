Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Find and Replacement
>>> words ="It's thanksgiving day.It's my birthday,tool!"
>>> index = words.find('day')
>>> print "index of Day = " ,index
index of Day =  18
>>> newstr= 'month'
>>> print words.replace("day",newstr)
It's thanksgiving month.It's my birthmonth,tool!
>>> 
>>> # Min and Max
>>> x = [2,54,-2,7,12,98]
>>> print min(x)
-2
>>> print max(x)
98
>>> # First and Last
>>> 
>>> x = ["hello",2,54,-2,7,12,98,"world"]
>>> print x[0]
hello
>>>  print x[len(x)-1]
 
  File "<pyshell#15>", line 2
    print x[len(x)-1]
    ^
IndentationError: unexpected indent
>>> print x[len(x)-1]
world
>>> print x[-1]
world
>>> 
>>> #New List
>>> 
>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> x.sort()
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> firsthalf = x[0:len(x)/2]
>>> secondhalf =x[len(x)/2:]
>>> print firsthalf
[-3, -2, 2, 6, 7]
>>> 
