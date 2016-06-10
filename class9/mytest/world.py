#!/usr/bin/env python


def func3():
    print "Hello from world.py"



class Myclass(object):


    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def repeat(self):
        return "{} {} ".format(self.a,self.b) * self.c



class MyChildClass (Myclass):
    def negate(self):
        return "No {} {} ".format(self.a, self.b) * self.c



class negative(Myclass):

    def __init__(self, a,b,c):
        self.a = 'New'
        self.b = 'World Order'
        self.c = c

    def changeme (self):
        return  (self.a + self.b) * self.c


def main():
    print "Executable code from world.py"


if __name__ == "__main__": main()
