def reverseTheNumber():

    for _ in range(int(input())):
        ans = 0
        n = int(input())
        while n > 0:
            ans = ans*10 + n%10
            n = n//10
        print(ans)

if __name__ == "__main__":
    reverseTheNumber()