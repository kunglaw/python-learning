first_name = "Aries Dimas"
last_name = "Yudhistira"

print("Hello, {} {} ".format(first_name, last_name))
print(f'Hello, {first_name} {last_name}')

print(first_name[2])
# python range, first index , last index which is not included
print(first_name[1:3])
print(len(first_name))


person = {
    "name": "Dimas",
    "age": 29

}

for i in first_name:
    print(i)

for o in person:
    key = str(o)
    print(f'{key} : {person[key]}')
