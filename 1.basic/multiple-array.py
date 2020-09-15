arr = []  # tipe data lis/array
num = 1

for i in range(5):

    arr.append([])
    for j in range(5):
        arr[i].append(num)
        num += 1

print(arr)

print(list(range(3, 10)))
