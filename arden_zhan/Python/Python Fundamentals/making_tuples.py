'''Dictionary in, tuples out'''
#function takes in dict, returns list of tuples
#first tuple is key, second is value

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
print my_dict.items()
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def dictToTuple(dict):
    tupleList = []
    for x in dict:
        newTuple = (x, dict[x])
        tupleList.append(newTuple)
    print tupleList

dictToTuple(my_dict)
