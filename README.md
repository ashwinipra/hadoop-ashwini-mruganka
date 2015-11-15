# Hadoop Programming By Ashwini Prabhu and Mruganka Londhe

## Airline Data

###### Problem1:
What is the percentage departures later than 5 minutes from every airport?

The program reads the input file line by line and splits the contents into single values. For this problem we are sending the city, estimated departure time and the actual departure time with a count, from the mapper to the reducer. In the reducer we are calculating the percentage of delayed flights for each airport.

The outpus is as follows.
```
The percentage of the flights that were delayed for more than 5 minutes at : Adak Island is 42%.	
The percentage of the flights that were delayed for more than 5 minutes at : Amarillo is 32%.	
The percentage of the flights that were delayed for more than 5 minutes at : Aspen is 35%.	
```

###### Problem2:
How many total hours of airtime did each carrier have?

The program reads the input file line by line and splits the contents into single values. For this problem we are sending the carrier and airtime, from the mapper to the reducer. In the reducer we are calculating the totals minutes of delay for each carrier.

The outpus is as follows.
```
The total time for carrier B6 is: 34913615.0	

The total time for carrier DL is: 93360030.0	

The total time for carrier UA is: 82973301.0		
```

## Twitter Data

The program reads the input file line by line. Then it creates a list of feature words from the line. Then it checks if the line contains the name of any of the presidential candidates that are hardcoded in the program. If a match is found then it is sent to the reducer in the following format.
```
print "LongValueSum:" + " Bernie Sanders" + ": " + classifier.classify(d) + "\t" + "1"
```
The screenshot is included in the output folder.
The outpus is as follows.
```
Ben Carson: neg	77291
Ben Carson: pos	60027
Bernie Sanders: neg	43275
Bernie Sanders: pos	22652
Donald Trump: neg	116754
Donald Trump: pos	58635
Hilary Clinton: neg	39171
Hilary Clinton: pos	25191
```



