'''Making and Reading from Dictionaries'''
#Dictionary Basics

#create dictionary containing info about youself. name, age, country of birth, fave language

me = {
    "name": "Arden",
    "age": 14,
    "birthCountry": "America",
    "faveLang": "Python"
}

def infoPrint(dict):
    print "Unordered"
    for x in dict:
        print "My {} is {}".format(x, dict[x])

    print "\nOrdered"
    print "My name is", me["name"]
    print "My age is", me["age"]
    print "My country of birth is", me["birthCountry"]
    print "My favorite language is", me["faveLang"]

infoPrint(me)