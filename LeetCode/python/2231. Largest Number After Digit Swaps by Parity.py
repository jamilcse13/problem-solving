def largestInteger():
    num = int(input())
    nums = list(map(int, str(num)))
    length = len(nums)
    odd = []
    even = []
    ans = 0

    while num > 0:
        n = num % 10
        if n % 2 != 0:
            odd.append(n)
            num = num//10
        else:
            even.append(n)
            num = num//10

    for i in range(length):
        if odd and nums[i] % 2 != 0:
            maxOdd = max(odd)
            ans = ans * 10 + maxOdd
            odd.remove(maxOdd)
        elif even:
            maxEven = max(even)
            ans = ans * 10 + maxEven
            even.remove(maxEven)
    print(ans)


if __name__ == "__main__":
    largestInteger()
