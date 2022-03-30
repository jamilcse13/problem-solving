def nestedLists():
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        m = arr[0]
        x = arr[1]
        y = arr[2]

        exp = list(map(int, input().split()))[:m]

        count = 0
        xy = x*y
        exp.sort()

        temp = exp[0] - xy
        if temp > 0:
            count += temp - 1

        post = xy + exp[0]

        for i in range(1, m):
            temp = exp[i]-xy
            if temp > post:
                count += temp - post - 1

            post = xy + exp[i]

        if post < 100:
            count += 100 - post

        print(count)

if __name__ == '__main__':
    nestedLists()