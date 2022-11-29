some_list = [1, 0.1, 'One']

print("Получение элементов из списка:")
print("Вывод всех элементов списка: {result}"               .format(result = some_list))
print("Вывод одного элемента из списка: {result}"           .format(result = some_list[0]))
print("Вывод элементов списка начиная со второго: {result}" .format(result = some_list[1:]))
print("Вывод элементов списка до третьего: {result}"        .format(result = some_list[:2]))
print("Вывод элементов списка через 1: {result}"            .format(result = some_list[::2]))
print("Вывод элементов списка в обратном порядке: {result}" .format(result = some_list[::-1]))

print("\nДобавление / Удаление элементов списка:")
some_list.append(2)
print("Расширение списка, добавив элемент в конец: {result}"            .format(result = some_list))
some_list.extend([0.2, 'Two'])
print("Расширение списка, добавив элементы из другого списка: {result}" .format(result = some_list))
some_list.insert(3, 666)
print("Расширение списка, добавив элемент в нужном месте: {result}"     .format(result = some_list))
some_list.remove(666)
print("Удаление элемента из списка: {result}"                           .format(result = some_list))
del some_list[3:]
print("Удаление элемента из списка (ячейки): {result}"                  .format(result = some_list))
some_list.append([2, 0.2, 'Two'])
print("Вывод одного элемента из списка ({value}): {result} "            .format(value = some_list, result = some_list[3][1]))
some_list.extend(range(10)) # range(0,10) range(0,10,2) range(10,0,-1)
print("Добавление диапазона от 0 до 9: {result}"                        .format(result = some_list))

print("\nДругие операции:")
print("Количество элементов списка: {result}"   .format(result = len(some_list)))
print("Количество 1 в списке: {result}"         .format(result = some_list.count(1)))
del some_list[0:4]
print("Минимальное значение в списке: {result}" .format(result = min(some_list)))
print("Максимальное значение в списке: {result}".format(result = max(some_list)))
some_list.extend(range(10,0,-1))
some_list.sort()
print("Отсортированный список: {result}"        .format(result = some_list))
some_list[0] = 666
print("Меняем значение первого элемента: с 0 на 666: {result}"        .format(result = some_list))

print("\n* — список является изменяемым объектом, в отлчичии от чисел и строк.")