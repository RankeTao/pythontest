# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
the iterator as range()
"""
class myRange(object):
    def __init__(self, n):
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
    
if __name__ == "__main__":
    x = myRange(7)
    print("x.next()==>", x.next())
    print("x.next()==>", x.next())
    print("-----for loop-----")
    for i in x:
        print(i)