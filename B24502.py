import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 10**21
a = [int(i) % k for i in input().split()]

np, nz, nn = (0, MAX), (0, MAX), (0, MAX)

def init() :
    global np, nz, nn
    np, nz, nn = (0, MAX), (0, MAX), (0, MAX)

def update(val, cnt) :
    global np, nz, nn
    if val > 0 : np = (val, min(np[1], cnt))
    elif val == 0 : nz = (val, min(nz[1], cnt))
    else : nn = (val, min(nn[1], cnt))

def sol() :
    if sum(a) % k : return "blobsad"
    ps, zr, ng = (0, MAX), (0, 0), (0, MAX)
    for i in a :
        init()
        val, cnt = ps
        if cnt != MAX :
            update((i + val) % k, cnt + val)
            update(i - (k - val), cnt + k - val)
        val, cnt = zr
        if cnt != MAX :
            update(i, cnt)
        val, cnt = ng
        if cnt != MAX : 
            update((i + val) % k, cnt - val)
        ps, zr, ng = np, nz, nn
    return zr[1]

print(sol())

"""

#import<iostream>
using namespace std;
long k,m,n,s,a[1000005];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n>>k;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i];
		s+=a[i];
	}
	if(s%k)
	{
		cout<<"blobsad";
		return 0;
	}
	s=0;
	for(int i=1;i<n;i++)
	{
		if(a[i]%k*2<k)
		{
			a[i+1]+=a[i]%k;
			s+=a[i]%k;
		}
		else
		{
			a[i+1]+=a[i]%k;
			s+=k-a[i]%k;
		}
	}
	cout<<s;
}

#include <iostream>
#define forin(i, n) for(int i = 0; i < n; ++i)
using namespace std;

int a[1000007];
int main(){
    cin.tie(0); ios::sync_with_stdio(0);
    int n, k; cin >> n >> k;
    long long s = 0;
    forin(i, n) cin >> a[i];
    long long su = 0; forin(i, n) su += a[i];
    if (su % k) {
        cout << "blobsad"; return 0;
    }
    int t = 0;
    forin(i, n){
        a[i] %= k;
        t += a[i];
        if(t >= k) t -= k;
        if(t < k - t) s += t;
        else s += k-t;
    }
    cout << s;
}
"""