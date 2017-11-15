class MathDojo(object):
    def __init__(self, start=0):
        self.value = start
    
    def add(self, *adds):
        for idx in adds:
            if isinstance(idx, int) or isinstance(idx, float):
                self.value+= idx
            elif isinstance(idx, list):
                self.value += sum(idx)
        return self

    def subtract(self, *subs):
        for idx in subs:
            if isinstance(idx, int) or isinstance(idx, float):
                self.value-= idx
            elif isinstance(idx, list):
                self.value -= sum(idx)
        return self

    def result(self):
        print (self.value)
        return self


md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md2 = MathDojo()

md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()





