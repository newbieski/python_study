import time

a1 = time.time()
print(a1)

a2 = time.localtime()
print(a2)

print(a2.tm_year, a2.tm_mon, a2.tm_mday, a2.tm_wday, a2.tm_yday)