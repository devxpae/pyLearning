some_value = [1, 0.1, 'One']

print("Получение элементов из списка:")
print("Вывод всех элементов списка: {result}"               .format(result = some_value))
print("Вывод одного элемента из списка: {result}"           .format(result = some_value[0]))
print("Вывод элементов списка начиная со второго: {result}" .format(result = some_value[1:]))
print("Вывод элементов списка до третьего: {result}"        .format(result = some_value[:2]))
print("Вывод элементов списка через 1: {result}"            .format(result = some_value[::2]))
print("Вывод элементов списка в обратном порядке: {result}" .format(result = some_value[::-1]))

print("\nДобавление / Удаление элементов списка:")
some_value.append(2)
print("Расширение списка, добавив элемент в конец: {result}"            .format(result = some_value))
some_value.extend([0.2, 'Two'])
print("Расширение списка, добавив элементы из другого списка: {result}" .format(result = some_value))
some_value.insert(3, 666)
print("Расширение списка, добавив элемент в нужном месте: {result}"     .format(result = some_value))
some_value.remove(666)
print("Удаление элемента из списка: {result}"                           .format(result = some_value))
del some_value[3:]
print("Удаление элемента из списка (ячейки): {result}"                  .format(result = some_value))
some_value.append([2, 0.2, 'Two'])
print("Вывод одного элемента из списка ({value}): {result} "            .format(value = some_value, result = some_value[3][1]))