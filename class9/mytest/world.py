#!/usr/bin/env python


def func3():
    print "Hello from world.py"



def main():
    print "Executable code from world.py"


if __name__ == "__main__": main()



class Myclass(object):


    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def repeat(self):
        return "{} {} ".format(self.a,self.b) * self.c




#class MyChildClass (Myclass):
    def negate(self):
        return "No {} {} ".format(self.a, self.b) * self.c




