from datetime import datetime, timedelta
from itertools import groupby
from decimal import *

data = []
with open("3B_1_sinPareamiento.txt", 'r') as f:
	for line in f:
		if "SEMAPHORE_WAIT" in line:
			info = line.split(',')
			data.append([info[0], info[2].split()])

results = ""

for k in data:
	results += "['{}',{}]".format(Decimal(data[1]), Decimal(Decimal(data[1]) - Decimal(data[0])))

with open("semaphore.txt", 'w') as f:
	f.write(results)

