# распечатайте все числа (должны быть только положительные), которые делятся на 3 без остатка от start до end(включительно) (start, end - могут быть перепутаны), start , end- гарантируется, что целые числа
# Найти в этом наборе числа, которые делится на три без остатка

start = 15
end = 5

if start > end:
    start, end = end, start

for number in range(start, end + 1):
    if number > 0 and number % 3 == 0:
        print(number)


# Напишите программу, которая подсчитывает количество каждого элемента в списке и выводит результат.

input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

count_dict = {}
for element in input_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

for element, count in count_dict.items():
    print(f"Элемент {element} встречается {count} раз(а)")
