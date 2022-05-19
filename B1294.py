#test
#a,*b=input().split()
#print(a, type(b))
# rafle code
n=int(input())
l=[]
ans = 0
for _ in range(n):
	s = input()
	ans += len(s)
	l.append(s + '~')
for i in range(ans):
	l.sort()
	print(l[0][0], end='')
	l[0] = l[0][1:]