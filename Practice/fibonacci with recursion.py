def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the range: "))
arr = []
for i in range(2,n):
    arr.append(fibonacci(i))
    print(arr)