some_string_a = 'qwertyuiop'
some_string_b = 'asdfghjkl'

print('Название')
print("Подходит для написания абзацев, большших фрагментов текста.")
print("ООО {companyName} — №1 на рынке IT.".format(companyName = '"Название компании"'))

print("\nОператоры сравнения:")
print("Длина объекта some_string_a — {valueA}, а some_string_b — {valueB}".format(valueA = len(some_string_a), valueB = len(some_string_b)))
print("({valueA} > {valueB}): {result}" .format(valueA = some_string_a, valueB = some_string_b, result = some_string_a > some_string_b))
print("({valueA} >= {valueB}): {result}".format(valueA = some_string_a, valueB = some_string_b, result = some_string_a >= some_string_b))
print("({valueA} < {valueB}): {result}" .format(valueA = some_string_a, valueB = some_string_b, result = some_string_a < some_string_b))
print("({valueA} <= {valueB}): {result}".format(valueA = some_string_a, valueB = some_string_b, result = some_string_a <= some_string_b))
print("({valueA} == {valueB}): {result}".format(valueA = some_string_a, valueB = some_string_b, result = some_string_a == some_string_b))
print("({valueA} != {valueB}): {result}".format(valueA = some_string_a, valueB = some_string_b, result = some_string_a != some_string_b))

print("\n* — с объектами типа String (str) возможно производить те же операции, что и с объектами типа Numbers (int, float, ...).")

print("\nИндексация строк:")
print("Вывод 1 символ объекта some_string_a: {result}"                    .format(result = some_string_a[0]))
print("Вывод с 1 по 4 символ объекта some_string_a: {result}"             .format(result = some_string_a[0:4]))
print("Вывод символов объекта some_string_a через 1: {result}"            .format(result = some_string_a[::2]))
print("Вывод символов объекта some_string_a в обратном порядке: {result}" .format(result = some_string_a[::-1]))

print("\nКодирование / Декодирование:")
some_string_c = 'йцукен'.encode()
print("Строка: {value}, была закодирована и декодирована (Кодировка: по умолчанию (UTF-8.)). Результат: {result}".format(value = some_string_c, result = some_string_c.decode()))