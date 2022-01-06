import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
s = input()
hh = []
pp = []
ans = 0
for i in range(n) :
    
    if s[i] == 'H' :
        while len(pp) > 0 and i - pp[0] > k :
            pp.pop(0)
        if len(pp) > 0 :
            ans += 1
            pp.pop(0)
        else : 
            hh.append(i)
    else :
        while len(hh) > 0 and i - hh[0] > k :
            hh.pop(0)
        if len(hh) > 0:        
            ans += 1
            hh.pop(0)
        else :
            pp.append(i)
print(ans)

n, k = map(int, input().split())
inp = list(input())
res = 0
for i in range(n):
  if inp[i] == 'P':
    for j in range(i-k,i+k+1):
      if 0<=j<n and inp[j]=='H':
        res += 1
        inp[j]='X'
        break
print(res)