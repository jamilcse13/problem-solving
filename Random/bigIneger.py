"""
Approach:
- first I take two inputs n and m (m>n)
- then I fixed the Fibonacci iteration limit between n and m
- create an array arr of Fibonacci series on that limit using fibonacci() recursive function
- finally, iterate arr and calculate the odd and even number
- return the output


Time Complexity: m - n
"""

def bigIneger():

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    for k in range(int(input())):
        n, m = map(int, input().split())
        arr = []

        for i in range(n-1,m):
            arr.append(fibonacci(i))

        Odd = 0
        Even = 0
        for i in arr:
            if i%2 == 0:
                Even += 1
            else:
                Odd += 1

        print("Case " + str(int(k+1)) + ":")
        print("Odd = " + str(int(Odd)))
        print("Even = " + str(int(Even)))

if __name__ == "__main__":
    bigIneger()