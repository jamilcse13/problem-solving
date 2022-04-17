def chefAndOperators():

    for _ in range(int(input())):
        (a, b) = map(int, input().split(' '))
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')

if __name__ == "__main__":
    chefAndOperators()