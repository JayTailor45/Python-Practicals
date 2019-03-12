length = int(input('Enter number of elements :'))
arr, pos, neg = [], [], []
n = 0
for x in range(0,length):
    el = int(input('Enter a number'))
    arr.append(el)

for x in range(len(arr)):
    if arr[x] > 0:
        pos.append(arr[x])
    else:
        neg.append(arr[x])

print('Original sorted numbers',arr)
pos.sort()
print('Positive sorted numbers',pos)
neg.sort()
print('Negative sorted numbers',neg)