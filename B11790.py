import sys
import math
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
MOD = 1000000007
SZ = (2**20)
vt = [True for _ in range(10**7 + 1)]
pr = []
for i in range(2, int(math.sqrt(10**7))) :
    if vt[i] :
        for j in range(i * i, 10**7 + 1, i) :
            vt[j] = False
for i in range(2, 10**7 + 1) :
    if vt[i] :
        pr.append(i)

tr = [1 for _ in range(SZ * 2)]
def idx_init() :
    for i in range(len(pr)) :
        tr[i + SZ] = pr[i]
    for i in range(SZ - 1, 0, -1) :
        tr[i] = tr[i * 2] * tr[i * 2 + 1] % MOD
idx_init()

def idx_mul(l, r) :
    l += SZ
    r += SZ
    res = 1
    while l <= r :
        if l & 1 :
            res *= tr[l]
            res %= MOD
        l = (l + 1) // 2
        if r & 1 == 0 :
            res *= tr[r]
            res %= MOD
        r = (r - 1) // 2
    return res

def mylog(p, n) :
    res = 0
    while p <= n :
        res += 1
        n //= p
    return res

def mysearch(n, k) :
    l, r = 0, len(pr) - 1
    res = 0
    while l <= r :
        mid = (l + r) // 2
        tmp = mylog(pr[mid], n)
        if tmp < k : r = mid - 1
        elif tmp == k :
            res = max(res, mid)
            l = mid + 1
        else : l = mid + 1
    return res
"""
def sol1(n) :
    ans = 1
    prev = 0
    for j in pr :
        tmp = mylog(j, n)
        if tmp <= 1 :
            break
        prev = tmp
        ans *= pow(j, tmp - 1, MOD)
        ans %= MOD
    return ans
"""
def sol2(n) :
    ans = 1
    i = 0
    while i < len(pr) :
        tmp = mylog(pr[i], n)
        if tmp <= 1 : break
        j = mysearch(n, tmp)
        mul = idx_mul(i, j)
        ans *= pow(mul, tmp - 1, MOD)
        ans %= MOD
        i = j + 1
    return ans

t = int(input())
for tc in range(1, t + 1) :
    n = int(input())
    #ans = sol1(n)
    ans2 = sol2(n)
    print(f'Case {tc}: {ans2}')


    #include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const long long m = 1e9 + 7;
const long long big = 1e14;
vector<pair<long long, long long>> prime;
bool check[10000001];
long long prep[10000001], N, T;
int main() {
	cin.tie(0)->sync_with_stdio(0);
	prime.push_back({1, 1});
	for (long long i=2; i<10000001; i++) {
		if (check[i] == 0) {
			for (long long j=i*i; j<10000001; j+=i) check[j] = 1;
			long long tmp = i;
			while (tmp <= big/i) {
				tmp *= i;
				prime.push_back({tmp, i});
			}
		}
	}
	sort(prime.begin(), prime.end());
	//for (int i=0; i<=100; i++) cout << prime[i].first << " " << prime[i].second << "\n";
	prep[0] = 1;
	for (int i=1; i<prime.size(); i++) prep[i] = prep[i-1] * prime[i].second % m;
	//for (int i=0; i<=100; i++) cout << prep[i] << "\n";
	//cout << prime[prime.size()-1].first << "\n";
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N;
		int lo = 0, hi = (int)prime.size()-1, ans;
		//for (int i=0; i<1000; i++) {
		//if (N >= 4) {
			while (lo <= hi) {
				int mid = (lo + hi) / 2;
				//cout << lo << " " << hi << " " << mid << "\n";
				if (prime[mid].first <= N) {
					ans = mid;
					lo = mid + 1;
				}
				else hi = mid - 1;
			}
			cout << "Case " << t << ": " << prep[ans] << "\n";
		//}
		//else cout << "Case " << t << ": " << 1 << "\n";
		//cout << prime[ans-1].first << " "<< prime[ans].first << " " << prime[ans+1].first << "\n"; 
		//cout << prep[ans-1] << " "<< prep[ans] << " " << prep[ans+1] << "\n"; 
		
	}
}