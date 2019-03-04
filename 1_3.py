n = int(input('Enter a number : '))

x = 0
sum = 0
a = 0
b = 1


def fibo(n):
    global a, b, x, sum
    if n > 0:
        sum = a + b
        a, b = b, sum
        print(sum)
        fibo(n-1)


fibo(n)
