#!/usr/bin/env python


import mytest
from mytest import Myclass,MyChildClass,negative



def main():

    word = negative('Hello','World',2)
    print word.changeme()

    word2 = Myclass('Hello','World', 2)
    print word2.repeat()
    
    word3 = MyChildClass('Hello','World',2)
    print word3.negate()



if __name__ == "__main__": main()


