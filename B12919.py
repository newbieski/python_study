import sys
import queue
sys.stdin = open("input.in", "r")
here = input()
there = input()
q = queue.Queue()
q.put(there)
ans = 0
while not q.empty() :
    cur = q.get()
    if len(cur) == len(here) :
        if cur == here :
            ans = 1
            break
    else :
        if cur[-1] == 'A' :
            q.put(cur[0:-1])
        if cur[0] == 'B' :
            q.put(cur[1:][::-1])
print(ans)
