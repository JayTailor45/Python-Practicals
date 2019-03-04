value = int(input('Enter a number : '))


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


msg = ' is Prime number.' if isPrime(value) else ' is Not Prime number'

print(str(value) + msg)
