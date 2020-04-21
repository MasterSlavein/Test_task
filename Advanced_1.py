# a = []
# n = int(input())
# for i in range(n):
    #new_element = int(input())
    #a.append(new_element)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = 0
odd_numbers = 0
for element in a:
    if element % 2 == 0:
        even_numbers += 1
    elif element % 2 == 1:
        odd_numbers += 1
print(f'number of odd numbers is equal to {odd_numbers} \nnumber of even numbers is equal to {even_numbers}')
