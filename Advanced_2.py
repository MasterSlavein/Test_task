a = int(input())
b = int(input())
if a < b:
    a, b = b, a
num_sum = 0
for element in range(b, a + 1):
    num_sum += element
print(num_sum)

