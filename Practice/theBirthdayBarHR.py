import math

n = int(input())

s = list(map(int, input().split()))[:n]
nums = list(map(int, input().split()))
d = nums[0]
m = nums[1]

length = len(s)
ans = 0
val = 0

if length == 1:
    if s[0] == d:
        print(1)
    else:
        print(0)
        raise SystemExit
    
for i in range(0, m):
    val += s[i]
if val == d:
    ans += 1

for i in range(1, length-m+1):
    val = val - s[i-1] + s[i+m-1]
    if val == d:
        ans += 1
print(ans)
