#Multiples
# part 1 odd numbers from 1 to 1000

for element in range(0,1000):   # for loop start 0 to 1000
		if element%2==1:    # checking odd numbers
				print "Odd Number 1 to 1000=",element # print all odd number 1 to 1000



#  Part 2  prints all the multiples of 5 from 5 to 1,000,000.

for element in range(5,1000001):# loop start from 5 to 100000001 ,if i change 1000000 then loop print value less then 10000000
   if(element % 5 == 0):  #check the Modulus of 5
    print "multiple of 5 =", element    #print the multiple of 5


# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]   # value of list
print sum(a) # using the built in function sum to calculate sum of all the value in list

#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]       # value in the list
print sum(a)/len(a)             # use bulit in function sum() to add all value in the list and then divide by total length of the list 
