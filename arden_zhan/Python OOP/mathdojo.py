'''Math Dojo'''

class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self, *args):
        for x in args:
            if isinstance(x, list) or isinstance(x, tuple):
                self.result += sum(x)
            else: self.result += x
        return self

    def subtract(self, *args):
        for x in args:
            if isinstance(x, list) or isinstance(x, tuple):
                self.result -= sum(x)
            else: self.result -= x
        return self

print "\nPart 1"
md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

print "\nPart 2 and 3"
md2 = MathDojo()
print md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
print md2.add((1, 2, 3)).subtract((1, 4, 5)).result