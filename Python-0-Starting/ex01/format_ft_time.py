import time

# time.gmtime() returns the time as object     
# time.time() return seconds since epoch

monthEpoch = time.strftime("%B", time.gmtime(0))
dayOfMonthEpoch = int(time.strftime("%d", time.gmtime(0)))
yearEpoch = time.strftime("%Y", time.gmtime(0))
secondsSinceEpoch = time.time()
formatSeconds = "{:,.4f}".format(secondsSinceEpoch)
scientificSeconds = "{:.2e}".format(secondsSinceEpoch)

print(f"Seconds since {monthEpoch} {dayOfMonthEpoch}, "
    f"{yearEpoch}: {formatSeconds} or {scientificSeconds} "
    f"in scientific notation")
print(time.strftime("%b %d %Y", time.gmtime()))


# resource:
# - https://docs.python.org/3/library/time.html#module-time
# - https://www.w3schools.com/python/ref_string_format.asp
# - https://www.w3schools.com/python/python_datetime.asp
# - https://www.geeksforgeeks.org/python-time-module/