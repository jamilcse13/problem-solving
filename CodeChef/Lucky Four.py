def luckyFour():

    for _ in range(int(input())):
        count = 0
        n = int(input())
        while n > 0:
            if n%10 == 4:
                count += 1
            n = n//10
        print(count)

if __name__ == "__main__":
    luckyFour()