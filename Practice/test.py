# n = int(input())
# print(n)

# l = list(map(int, input().split()))
# print(l)

# arr = list(map(int, input().split()))[:n]
# print(arr)


def summation():
    # t = int(input())

    # while t:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))[:n]
        ans = first = 0
        last = len(arr)-1
        
        while first < last:
            ans += arr[first] + arr[last]
            first += 1
            last -= 1
        
        if last%2 != 0:
            ans += arr[(last+1)//2]

        print(ans)

        # t -= 1

if __name__ == "__main__":
    summation()