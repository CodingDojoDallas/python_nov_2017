#Fun with Functions

'''Odd/Even'''
# counts from 1 to num and prints whether it's odd or even.
def odd_even(num):
    state = ""
    for x in range(1, num + 1):
        if (x % 2 == 1): state = "odd"
        else: state = "even"
        print "Number is {}. This is an {} number.".format(x, state)
odd_even(20)

'''Multiply'''
# iterates through each list value and returns list with each value multiplied by 5
def multiply(ls, mult):
    for val in range(len(ls)):
        ls[val] *= mult
    return ls
print multiply([2,4,10,16], 5)

'''Hacker Challenge'''
# takes multiply func call as an argument. returns multiplied list as 2D list. 
# each internal list should contain 1's times number in original list
def layered_multiples(arr):
    new_array = []
    for val in range(len(arr)):
        new_array.append([1]*arr[val])
    return new_array
x = layered_multiples(multiply([2,4,5], 3))
print x