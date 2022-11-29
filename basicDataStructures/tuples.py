some_tuple = (0, 0.1, 1, 2, 3, 4, 5)

print("Получение элементов из кортежа:")
print("Вывод всех элементов кортежа: {result}"               .format(result = some_tuple))
print("Вывод одного элемента из кортежа: {result}"           .format(result = some_tuple[0]))
print("Вывод элементов кортежа начиная со второго: {result}" .format(result = some_tuple[1:]))
print("Вывод элементов кортежа до третьего: {result}"        .format(result = some_tuple[:2]))
print("Вывод элементов кортежа через 1: {result}"            .format(result = some_tuple[::2]))
print("Вывод элементов кортежа в обратном порядке: {result}" .format(result = some_tuple[::-1]))

print("\nДругие операции:")
print("Количество элементов кортежа: {result}"   .format(result = len(some_tuple)))
print("Количество 1 в кортеже: {result}"         .format(result = some_tuple.count(1)))
print("Минимальное значение в кортеже: {result}" .format(result = min(some_tuple)))
print("Максимальное значение в кортеже: {result}".format(result = max(some_tuple)))

print("\n* — кортеж является неизменяемым объектом, как числа и строки.")