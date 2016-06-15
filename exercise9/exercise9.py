#!/usr/bin/env python


import mytest
from mytest.simple import func1
from mytest.whatever import func2
from mytest import Myclass,MyChildClass,negative



def main():

    word = negative('Hello','World',2)
    print word.changeme()

    word2 = Myclass('Hello','World', 2)
    print word2.repeat()
    
    word3 = MyChildClass('Hello','World',2)
    print word3.negate()

    mytest.func1()
    mytest.func2()
    mytest.func3()



if __name__ == "__main__": main()


