"""
Approach:
- first, I took two inputs x and y
- iterate min value to max value between x and y
- check is it a palindrome or not
- increase the count if it is a palindrome
- finally, print the output


Time Complexity: (m - n) * length of m
"""

def FfindPalindrome():

    for k in range(int(input())):
        x, y = map(int, input().split())
        count = 0

        for i in range(min(x,y), max(x,y)+1):
            if str(i) == str(i)[::-1]:
                count += 1

        print("Case " + str(int(k+1)) + ": " + str(int(count)))

if __name__ == "__main__":
    findPalindrome()