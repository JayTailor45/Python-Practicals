value = input('Enter a number : ')


def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str


print('Reverse of ' + value + ' is ' + reverse(value))
