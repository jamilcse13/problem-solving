def nestedLists():
    hashMap = {}
    hashset = set()
    ans = []
    
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        hashMap[name] = score
        hashset.add(score)
    
    second_lowest = sorted(hashset)[1]
    
    for key, val in hashMap.items():
        if val == second_lowest:
            ans.append(key)
    
    for i in sorted(ans):
        print(i)

if __name__ == '__main__':
    nestedLists()