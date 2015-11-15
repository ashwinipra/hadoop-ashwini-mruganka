#!/usr/bin/python
#
#  What is the percentage departures later than 5 minutes from every airport?


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
            if wrds[10] !='':
                print wrds[3]+ '\t'+ wrds[9]+'\t'+wrds[10] + '\t' + "1"
            line = sys.stdin.readline()


except "end of file":
    return None

if __name__ == "__main__":
    main(sys.argv)





