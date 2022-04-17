def firstAndLastDigit():

    for _ in range(int(input())):
        n = int(input())
        s = str(n)
        ans = int(s[0]) + int(s[len(s)-1])
        print(ans)

if __name__ == "__main__":
    firstAndLastDigit()