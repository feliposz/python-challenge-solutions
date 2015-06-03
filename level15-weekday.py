import datetime

year = 1006
month = 1
day = 27 # todo: buy flowers for tomorrow (26 + 1, tuesday)

while (year < 2000):
	mydate = datetime.date(year, month, day)
	if mydate.weekday() == 1:
		print(year)
	year += 10

saidas = """
1046
1176
1226
1356
1446
1576
1626
1756
1846
1976
"""

#http://en.wikipedia.org/wiki/January_27
#1756 – Wolfgang Amadeus Mozart, Austrian composer (d. 1791)
