value = input('Enter a number : ')


def isArmstrong(n):
    lists = list(n)
    length = len(n)
    sum = 0

    for x in range(len(lists)):
        sum += pow(int(lists[x]), length)

    if sum == int(n):
        return True
    else:
        return False


print('Armstrong number' if isArmstrong(value) else 'Not a Armstrong number')
