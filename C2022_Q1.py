tt=int(input())
a="-+"*19
b=".|"*19
for tc in range(tt):
  n,m=map(int,input().split())
  print(f'Case #{tc + 1}:')
  m=m*2
  print("..+"+a[:m - 2])
  print("."+b[:m])
  print("+"+a[:m])
  for _ in range(n-1):
      print("|"+b[:m])
      print("+"+a[:m])