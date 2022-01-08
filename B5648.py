import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
buf = []
bi = 1
    
def readone() :
    global buf
    global bi
    if bi >= len(buf) :
        buf = []
        while len(buf) == 0 :
            buf = input().split()
        bi = 0
    res = buf[bi]
    bi += 1
    return res

n = int(readone())
a = [0] * n
for i in range(n) :
    a[i] = int(readone()[::-1])
a.sort()
for i in a :
    if i : print(i)

import sys;[*map(print,sorted(map(int,sys.stdin.read()[::-1].split()[:-1])))]

import sys
f=lambda x:map(int,x[::-1].split())
*a,n=f(input())
for i in sys.stdin:a+=[*f(i)]
print(*sorted(a),sep='\n')

from sys import*
input = stdin.readline
def regist(arr):
    for x in arr:
        temp=''
        temp=x[::-1]
        res.append(int(temp))
          
a=list(map(str,input().split()))
n=int(a[0])
res=[]
if len(a)>1:regist(a[1:])
while 1:
    inp=list(map(str,input().split()))
    regist(inp)
    if len(res)==n: break
res.sort()
for i in range(n):
    print(res[i])