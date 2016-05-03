import test

class ConvData:

    def __init__(self):
        self.cls = dict()
        self.parlst = list()

    def gparent(self, val):
        if self.cls[val] is not None:
            print('* ' + str(self.cls[val]))
            for p in self.cls[val]:
                print(' - ' + str(p))
                self.gparent(p)
        else:
            print('add ' + str(val))
            self.parlst.append(val)

x = ConvData()
x.cls = {'13': ['11', '20'],
         '11': ['10'],
         '10': None,
         '20': ['7'],
         '7': None}

x.gparent('13')
print(x.parlst)
