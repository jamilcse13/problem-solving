def upperlower():
    s = input()

    arr = s.split(" ")
    ans = ''

    for word in arr:
        a = word[0]

        for i in range(1,len(word)):
            if ord(word[i-1].lower()) == ord(word[i].lower()):
                a += word[i]
            elif ord(word[i-1].lower()) < ord(word[i].lower()):
                a += word[i].upper()
            else:
                a += word[i].lower()
        ans += a + ' '

    return ans


if __name__ == "__main__":
    upperlower()