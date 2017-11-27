#!/usr/bin/python

import time
from datetime import datetime
#f = open("test.txt","w+")
f = open("test.txt","a")

while True:
    f.write("Time right now: %s\r\n" % str(datetime.now()) )
    time.sleep(5)

f.close()
