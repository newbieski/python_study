# star
for i in range(1,int(input())+1): print('*'*i)

# a + b
import sys

input()
s = list(sum(map(int, n.split())) for n in sys.stdin)

for n in s:
  print(n)


# freopen
import sys
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')
