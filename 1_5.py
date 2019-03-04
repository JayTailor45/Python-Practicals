string = input('Enter a string : ')

sbstr = input('Enter a sub-string to find in a string : ')


def substr(a, b):
    return a.index(b)


print(substr(string, sbstr))
