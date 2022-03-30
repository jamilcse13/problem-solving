import bisect


def activityNotifications():
    arr = list(map(int, input().split()))
    n = arr[0]
    d = arr[1]
    exp = list(map(int, input().split()))[:n]

    count = 0

    temparr = sorted(exp[0:0 + d])

    mid = d // 2

    if d % 2 != 0:
        temp = temparr[mid]
    else:
        temp = (temparr[mid - 1] + temparr[mid]) / 2

    if exp[0 + d] >= temp + temp:
        count += 1

    for i in range(1, n - d):

        temparr.remove(exp[i - 1])
        bisect.insort(temparr, exp[i + d - 1])

        mid = d // 2

        if d % 2 != 0:
            temp = temparr[mid]
        else:
            temp = (temparr[mid - 1] + temparr[mid]) / 2

        if exp[i + d] >= temp + temp:
            count += 1

    print(count)


if __name__ == '__main__':
    activityNotifications()
