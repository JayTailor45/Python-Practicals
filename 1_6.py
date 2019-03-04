n = int(input('Enter the hight : '))


def pattern(n):
    k = 2*n - 2
    for i in range(1, n):
        for j in range(1, k):
            print(end=" ")
        k = k - 1
        for j in range(1, i+1):
            print(str(i) + ' ', end="")
        print("\r")


pattern(n+1)
