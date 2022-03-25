import math
t = int(input())
 
while t:
    inp = list(map(int, input().split()))
    n = inp[0]
    c = inp[1]
    m = inp[2]
    ans = temp = n//c
    
    while temp >= m:
        ans += temp//m
        temp = (temp%m) + temp//m
    
    print(ans)

    t = t-1