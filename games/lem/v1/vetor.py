#!/usr/bin/env python

class Vetor:
    def __init__(self, x=0, y=0, z=None):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, v2):
        x = self.x + v2.x    
        y = self.y + v2.y    
        if self.z is None:
            return Vetor(x, y)    
        else:
            z = self.z + v2.z
            return Vetor(x, y, z)    
        
    def __getitem__(self, i):
        if self.z is None:
            return (self.x, self.y)[i]
        else:
            return (self.x, self.y, self.z)[i]

    def __repr__(self):
        return 'Vetor%s' % (tuple(self),)
        
if __name__ == '__main__':
    a = Vetor(1,2)
    b = Vetor(3,4)
    v = Vetor(5,6,7)
    c = a + b
    print a
    print a[0]
    print a[1]
    print tuple(a)
    print c
    print v           
