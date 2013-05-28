#!/usr/bin/env python

#!/usr/bin/env python

import MapReduce
import sys

"""
print pairs of assymetric friends a person has Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = "".join(sorted(record[0]+record[1]))
    value = []
    value.append(record[0])
    value.append(record[1])
    mr.emit_intermediate(key,value)

def reducer(key, value):
    if len(value)==1:
        x =[]
        x.append(value[0][1])
        x.append(value[0][0])
        x1 = tuple(x)
        x2 = tuple(value[0])
        mr.emit(x1)
        mr.emit(x2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
