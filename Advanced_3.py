from random import randint


a = []
for i in range(10):
    a.append(randint(1, 20))
a.sort()
print(a)

desired_value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != desired_value and low <= high:
    if desired_value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Current value does not exist")
else:
    print("Index =", mid)
