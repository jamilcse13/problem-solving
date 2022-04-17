def findRemainder():

    for _ in range(int(input())):
        (n, k) = map(int, input().split(' '))
        print(n%k)

if __name__ == "__main__":
    findRemainder()