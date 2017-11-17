mix_list = ['magical unicorns',19,'hello',98.98,'world']
int_list = [1,2,3,4,5]
str_list = ["Spiff", "Moon", "Robot"]


def identify_listType(list):
    new_string = ''
    total = 0


    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String:",new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_listType(mix_list)
print identify_listType(int_list)
print identify_listType(str_list)