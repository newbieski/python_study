import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
s = input().strip()
cur = 0
a = []
for i in s :
    if i == '(' : cur += 1
    else : cur -= 1
    a.append(cur)
if cur < 0 :
    ans = 0
    for i in range(len(s)) :        
        if s[i] == ')' : ans += 1
        if a[i] < 0 : break
    print(ans)
else :
    ans = 0
    for i in range(len(s) - 1, -1, -1) :
        if cur <= 0 : break
        if s[i] == '(' : ans += 1
        cur = min(cur, a[i])
    print(ans)