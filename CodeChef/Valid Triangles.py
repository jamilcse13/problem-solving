def sumOfDigits():

    for _ in range(int(input())):
        (a,b,c) = map(int, input().split(' '))
        if a+b+c == 180:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    sumOfDigits()