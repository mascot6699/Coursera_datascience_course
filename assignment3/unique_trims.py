#!/usr/bin/env python

import MapReduce
import sys

"""
trim last 10 letters and eliminate duplicate in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    value1 = value[:-10]
    mr.emit_intermediate(1, value1)

def reducer(key, values):
    # key: word
    # value: list of occurrence counts
    total =[]
    for v in values:
        if v not in total:
          total.append(v)
        
        
    for i,v in enumerate(total):
        mr.emit(total[i])
    
        
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
