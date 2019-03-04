n = input('Enter a number : ')

list = list(n)
sum = 0
for x in range(len(list)):
    sum = sum + int(list[x])
print(sum)
