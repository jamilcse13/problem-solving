"""
Approach:
- first, I took two inputs t and nums
- created a hashMap whose keys between 1 to 7 and values of each key is 0
- iterate the the given nums and store the volumes of each numbers
- then i checked the process in these conditions
    - as there have not to be numbers 5 and 7 in the nums array, as the are not divisible by any numbers between 2 to 7
    - volumes of 2 have to be greater or equal 4
    - volumes of 1 have to be equal to volume of 4 and 6
    - volume of 2 and 3 have to be equal to volume of 4 and 6
- finally i used 3 portions to print the output which could be the possible output in separate conditions


Time Complexity: n
"""

def findTupples():

    t = int(input())
    nums = list(map(int, input().split()))[:t]
    hashMap = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0
    }

    for i in nums:
        hashMap[i] += 1
    
    if hashMap[5] == 0 and hashMap[7] == 0 and hashMap[2] >= hashMap[4] and hashMap[1] == hashMap[4] + hashMap[6] and hashMap[2] + hashMap[3] == hashMap[4] + hashMap[6]:
        for i in range(hashMap[4]):
            print("1 2 4")
        hashMap[2] -= hashMap[4]

        for i in range(hashMap[2]):
            print("1 2 6")
        
        for i in range(hashMap[3]):
            print("1 3 6")
    else:
        print("-1")

if __name__ == "__main__":
    findTupples()