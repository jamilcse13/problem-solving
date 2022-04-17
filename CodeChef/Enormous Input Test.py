def enormousInputTest():
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    # (n, k) = map(int, input().split(' '))
    count = 0

    for _ in range(n):
        num = int(input())
        if num%k == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    enormousInputTest()