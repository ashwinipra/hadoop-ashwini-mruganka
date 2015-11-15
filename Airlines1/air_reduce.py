#!/usr/bin/python
#
#  What is the percentage departures later than 5 minutes from every airport?
import sys

city_list = list()
delay_list = {}
total_list = {}
total = 0
delayed_fl = 0
## collect (key,val) pairs from sort phase
for line in sys.stdin:
    
    try:
        city, val1, val2, count = line.strip().split("\t")
        
        #print carrier+" "+val1
        if city not in city_list:
            if int(val2) - int(val1) > 5 :
                city_list.append(city);
                delay_list[city] = int(count)
            total_list[city] = int(count)
        else:
            if int(val2) - int(val1) > 5 :
                delay_list[city] += int(count)
            total_list[city] += int(count)
        #print line
        total += 1
    except ValueError, err:
        sys.stderr.write("Value ERROR: %(err)s\n%(data)s\n" % {"err": str(err), "data": line})
for city in city_list:
    perc = delay_list[city] * 100 / total_list[city]
    print "The percentage of the flights that were delayed for more than 5 minutes at : "+city+" is " + str(perc)+"%."