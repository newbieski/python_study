import sys
import math

MOD = 10**9+7
tot = math.factorial(10)
cc = math.comb(5, 2) * math.comb(3, 2) * math.factorial(8) + math.comb(5, 2) * 6 * math.factorial(6) +  math.comb(5, 2) * 6 * math.factorial(7)
g = math.gcd(tot, cc)
print(tot, cc)
tot //= g
cc //= g
print(tot, cc)
inv = pow(tot, MOD - 2, MOD)
print("inv", inv, tot * inv % MOD)
ans = cc * inv % MOD
print(ans)