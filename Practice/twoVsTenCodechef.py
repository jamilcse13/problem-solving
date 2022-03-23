import math
t = int(input())
 
while t:
    n = int(input())
    
    if n%10 == 0:
        print(0)
    elif n%10 == 5:
        print(1)
    else:
        print(-1)
    
    t = t-1