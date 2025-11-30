n = int(input())
name = {}

for i in range(int(n)):
    user = input()
    if user not in name:
        name[user] = 0
        print("OK")
    else:
        name[user] += 1
        print(user + str(name[user]))

# print(name)    