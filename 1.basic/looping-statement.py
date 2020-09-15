myNumbers = [1, 2, 3, 4, 5, 6]

for num in myNumbers:
    print(num)

myItem = {
    "code1": 'GTX 1000',
    "code2": "AZROCK 500",
    "code3": "apple pro"
}

for item in myItem:
    print(item, " => ", myItem[item])

# looping in a tuple

myTupleList = [(1, 2), (3, 4), (5, 6)]

for (tup1, tup2) in myTupleList:
    print(tup1, " > ", tup2)
