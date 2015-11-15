#!/usr/bin/python
#
#  How many total hours of airtime did each carrier have?
import sys

carrier_list = list()
air_list = {}
total = 0
delayed_fl = 0
## collect (key,val) pairs from sort phase
for line in sys.stdin:
    
    try:
        carrier, val1= line.strip().split("\t")
        #print carrier+" "+val1
        if carrier not in carrier_list:
            carrier_list.append(carrier);
            air_list[carrier] = float(val1)
        else:
            air_list[carrier] += float(val1)
    except ValueError, err:
        sys.stderr.write("Value ERROR: %(err)s\n%(data)s\n" % {"err": str(err), "data": line})

for carrier in carrier_list:
    print "The total time for carrier " + carrier + " is: " + str(air_list[carrier])+"\n"