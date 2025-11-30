n, k, l, c, d, p, nl, np = map(int,input().split())

total_drink = k*l

max_toasts = total_drink//nl

max_toast_from_limes = c*d
max_toast_from_salt = p//np

final = [max_toasts , max_toast_from_limes , max_toast_from_salt]
final = min(final)

result = final//n
print(result)