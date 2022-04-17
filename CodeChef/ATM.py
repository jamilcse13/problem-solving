def atm():

    a, b = map(float, input().split())
    a = int(a)
    if a+0.5 > b or a%5 != 0:
        print(float(b))
    elif a%5 == 0:
        amount = b-a-0.50
        print(float(amount))

if __name__ == "__main__":
    atm()