#!/usr/bin/python
#
#  How many total hours of airtime did each carrier have?


import sys
import re

def main(argv):
    line = sys.stdin.readline()
    
    try:
        while line:
            #for word in pattern.findall(line):
            words = line.split(",")
            wrds = list()
            for w in words:
                n = w.replace('"', '')
                #print n
                wrds.append(n)
            if wrds[14] !='':
                print wrds[1]+ '\t'+ wrds[14]
            line = sys.stdin.readline()


except "end of file":
    return None

if __name__ == "__main__":
    main(sys.argv)





