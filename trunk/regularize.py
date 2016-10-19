#!/usr/bin/env python
# ./regularize.py  ~/flow_model/data_sources/pos_tobis03.csv col limit | sort -g -k 3
# ./regularize.py  ~/flow_model/data_sources/pos_tobis03.csv  3    9   | sort -g -k 3

import os
import sys
import string

col   = int(sys.argv[2])
limit = float(sys.argv[3])
#
f = open(sys.argv[1])
lines = f.readlines()
for line in lines[1:]:
    data = map(float, string.split(line[:-3], ";"))
    if data[col] > limit:
        print data[1], data[0], data[col]
