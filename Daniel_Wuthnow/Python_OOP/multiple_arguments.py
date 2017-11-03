# def varargs(arg1, *args):
#   print "Got "+arg1+" and "+ ", ".join(args)
# varargs("one") # output: "Got one and "
# varargs("one", "two") # output: "Got one and two"
# varargs("one", "two", "three") # output: "Got one and two, three"


def varargs(arg1, *args):
	print "args is of " + str(type(args))
varargs("one", "two", "three") # output: args is of <type 'tuple'>
