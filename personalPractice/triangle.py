"""
Approach:
- i just think to solve a pattern

Time Complexity: O(n)
"""
def summation():
    
    for _ in range(int(input())):
        arr = list(map(int, input().split()))[:3]
        arr.sort()
        two_sum = arr[0] + arr[2]
        extra = 1 if two_sum%2 != 0 else 0
        
        if arr[1] > (two_sum//2 + extra):
            print('yes')
        else:
            print('no')
        

if __name__ == "__main__":
    summation()