li = list(map(int,input().split()))

uniq_color = set(li)
final = 4-len(uniq_color)
print(final)