"""
Approach:
- first i took the number of lands t and then the lands in an array acre
- then i calculate the half of all lands value as i can compare this value for nearest greater than the half of all lands value
- i took two variables land and total_acre_of_land
- i iterate a loop among the sorted acre of lands 
- sum the acre to the total_acre_of_land and check is it greater than the half (half of total acres)
- at the same time i also count the number of land
- when the total_acre_of_land is greater than the half, i just break the iteration and return the number of land



Time Complexity: n
"""

def getLand():

    t = int(input())
    acre = list(map(int, input().split()))[:t]

    half = sum(acre) / 2
    land = total_acre_of_land = 0
    for i, v in enumerate(reversed(sorted(acre))):
        total_acre_of_land += v
        land += 1
        if total_acre_of_land > half:
            break
    print(land)

if __name__ == "__main__":
    getLand()