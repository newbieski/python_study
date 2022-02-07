m = int(input())
s = ("Gimossi", "Messi")
l = [len(s[0]), len(s[1])]

def sol(fn, k) :
    if fn <= 1 : return s[fn][k - 1]
    if k <= l[fn - 1] : return sol(fn - 1, k)
    elif k == l[fn - 1] + 1 : return "Messi Messi Gimossi"
    else : return sol(fn - 2, k - l[fn - 1] - 1)

cur = 2
while True :
    tmp = l[cur - 1] + l[cur - 2] + 1
    l.append(tmp)
    if tmp >= 2**30 : break
    cur += 1

cur = 1
while l[cur] < m : cur += 1
print(sol(cur, m))

"""
a,b=692181267,1119972817
x='Messi Messi Gimossi'
m=int(input())-1
g=1
while g*m>12:g&=m!=a;m%=a+1;a,b=b+~a,a
print(-g&m-5and x[m+6]or x)

from bisect import bisect as bc
M = int(input())
R = [6,14]
while R[-1]<=2**30-1: R.append(R[-1]+R[-2])
while M>=14: M -= R[bc(R, M)-1]
if M == 0 or M == 6: print("Messi Messi Gimossi")
else: print("Messi Gimossi"[M-1])
"""