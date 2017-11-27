#!/usr/bin/python

import time
from datetime import datetime
#f = open("test.txt","w+")
f = open("test.txt","a")

while True:
    f.write("Time right now: %s\r\n" % str(datetime.now()) )
    time.sleep(5)

f.close()

############################

#!/usr/bin/python3

import time
#f = open("test.txt","w+")
f = open("test.txt","a")

for i in range(100):
   f.write("This is line %d\r\n" % (i))
   time.sleep(1)
   i += 1

f.close()
