#!/usr/bin/env python

import MapReduce
import sys

"""
Implementing
"SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id"
SQL statement in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order number
    # value: whole line
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, record):
    # key: order number
    # value: whole record
    
    for index ,a in enumerate(key):
        if(index==0):
            for i in range(1,len(record)):
                mr.emit(record[0]+record[i])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
