#!/usr/bin/env python

import sys

count_of_values = 0

previous_key = None

for line in sys.stdin:

    data = line.strip().split("\t")
    
    key, value = data

    if previous_key != None and previous_key != key:
        sys.stdout.write("{0}\t{1}\n".format(previous_key, count_of_values))
        
        count_of_values = 0

    count_of_values += float(value)
    
    previous_key = key


sys.stdout.write("{0}\t{1}\n".format(previous_key, count_of_values))
