def xenia_and_divisors():
    
    count = [0]*8
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    for i in arr:
        count[i] += 1
    
    if count[5] == 0 and count[7] == 0 and count[2] >= count[4] and count[1] == count[4] + count[6] and count[2] + count[3] == count[4] + count[6]:
        for i in range(count[4]):
            print("1 2 4")
        count[2] -= count[4];
        
        for i in range(count[2]):
            print("1 2 6")

        for i in range(count[3]):
            print("1 3 6")
    else:
        print("-1")

if __name__ == "__main__":
    xenia_and_divisors()