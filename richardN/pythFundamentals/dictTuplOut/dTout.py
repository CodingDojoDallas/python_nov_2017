# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print my_dict.items()

print "------------"

def tup(my_dict):
    new = []
    for x,y in my_dict.items():
        new.append((x,y))
print my_dict

# solution-one
# def making_tupes(the_dict):
#     the_list = []
#     # here, k and v will parse each tuple of key,value pairs returned by .iteritems()
#     for k, v in the_dict.iteritems():
#         the_list.append((k,v))
#     return the_list
# i dont understand the "solution" given.




#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
