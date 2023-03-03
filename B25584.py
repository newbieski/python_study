from collections import defaultdict
import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n=int(input())
dict=defaultdict(int)
s=set()
for _ in range(n) :
    for i in [4, 6, 4, 10] :
        for name in input().split() :
            dict[name] = dict[name] + i
            s.add(name)
ans=[]
for name in s :
    if name != "-" :
        ans.append(dict[name])
if len(ans) == 0 :
    print("Yes")
elif max(ans) - min(ans) <= 12 :
    print("Yes")
else :
    print("No")