import datetime
import sys
import math

sys.stdin = open("input.in", "r")
n = int(sys.stdin.readline())
dates = []

if n == 0:
    print(0)
    exit(0)

for i in range(n):
    temp = sys.stdin.readline().split()
    year, month, day = map(int, temp[0].split("/"))
    hour, min, sec = map(int, temp[1].split(":"))
    rate = int(temp[2])

    dates.append((datetime.datetime(year, month, day, hour, min, sec), rate))

dates.sort()
default = datetime.timedelta(days=365)

temp_up, temp_down = 0, 0
idx = n - 1
for i in range(n):
    now, target = dates[i], dates[-1]
    temp = (target[0] - now[0]) / default
    force = max(0.5 ** float(temp), 0.9 ** idx)

    temp_up += force * now[1]
    temp_down += force
    idx -= 1
    print(i + 1, temp, target[0] - now[0], temp_up, temp_down)

print(temp_up, temp_down)
print(round(temp_up / temp_down))