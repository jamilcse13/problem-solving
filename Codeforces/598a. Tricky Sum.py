"""
Approach:
- first I take an input number n
- then I caculate the total sum of n numbers
- then I deleted the numbers (*2) which are the power of two
- here I deleted each numbers (power of two). beacuse when i calculate the total numbers, these numbers are also added there
- run the delete operation until i get the power of two
- finally get result and return it


Time Complexity: n
"""

def powerOfTwo():
     
    for _ in range(int(input())):
        n = int(input())
        total = (n*(n+1))//2
        a = 1
 
        while a <= n:
            total -= 2*a
            a = 2*a
 
        print(total)
 
if __name__ == "__main__":
    powerOfTwo()