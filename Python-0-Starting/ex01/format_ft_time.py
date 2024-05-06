import time

# time.gmtime(0) returns the time as object

# time.time() return seconds since epoch



monthEpoch = time.strftime("%B", time.gmtime(0))
dayOfMonthEpoch = int(time.strftime("%d", time.gmtime(0)))
yearEpoch = time.strftime("%Y", time.gmtime(0))
secondsSinceEpoch = time.time()
formattedtime = "{:,}".format(secondsSinceEpoch)
print(formattedtime)


print(f"Second since {monthEpoch} {dayOfMonthEpoch}, {yearEpoch}: {secondsSinceEpoch}")




# resource:
#     - https://docs.python.org/3/library/time.html#module-time