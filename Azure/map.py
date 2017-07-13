#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for numb, record in enumerate(sys.stdin):
    if numb != 0 and numb!= 1:
	#strip the whitelines

        record = record.strip()

	#toeknize as only separated by comma

        record = record.split(",")

        vendor_name = record[0] #Get he vendor name

        trip_distance = record[4]#get trip distance

        Fare_Amt = record[12]

        Payment = record[11].lower()

        Date = (record[1])[0:10]

        Passenger_Count = record[3]
        
