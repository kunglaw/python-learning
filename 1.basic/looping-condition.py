import datetime


def print_time():
    print("Task Complete")
    print(datetime.datetime.now())
    print("")


people = ["Aries", "Dimas", "Yudhistira"]

index = 0

# while index < 10:
#     print("index => ", index)
#     index += 1

i = len(people)-1  # 3
# print(i)

while i >= 0:
    # print(" i => ", i)
    print(people[i])
    print_time()
    i -= 1
