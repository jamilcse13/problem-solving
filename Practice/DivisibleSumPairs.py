def divisibleSumPairs():
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    ar = list(map(int, input().split()))[:n]

    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i]+ar[j])%k == 0:
                count += 1
    
    return count

if __name__ == "__main__":
    print(divisibleSumPairs())