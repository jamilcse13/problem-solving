def findRunnersUpScore():
    n = int(input())
    arr = list(map(int, input().split()))
    maxval = max(arr)
    ans = -100
    first = 0
    last = n-1

    print(arr)
        
    while first < last:
        if arr[first] > ans and arr[first] < maxval:
            ans = arr[first]
        print(first, arr[last])
        
        if arr[last] > ans and arr[last] < maxval:
            ans = arr[last]
        
        first += 1
        last -= 1
    
    if n%2 != 0 and arr[n//2] > ans and arr[n//2] < maxval:
        ans = arr[n//2]
    
    print(ans)

if __name__ == "__main__":
    findRunnersUpScore()