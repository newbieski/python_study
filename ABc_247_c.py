n = int(input())

s = ["1"]
for i in range(1, 16) :
    s.append(s[i - 1] + " " + str(i + 1) + " " + s[i - 1])
print(s[n - 1])