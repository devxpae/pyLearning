someStringA = 'qwertyuiop'
someStringB = 'asdfghjkl'

print('Название')
print("Подходит для написания абзацев, большших фрагментов текста.")
print("ООО {companyName} — №1 на рынке IT.".format(companyName = '"Название компании"'))

print("\nОператоры сравнения:")
print("Длина объекта someStringA — {valueA}, а someStringB — {valueB}".format(valueA = len(someStringA), valueB = len(someStringB)))
print("({valueA} > {valueB}): {result}" .format(valueA = someStringA, valueB = someStringB, result = someStringA > someStringB))
print("({valueA} >= {valueB}): {result}".format(valueA = someStringA, valueB = someStringB, result = someStringA >= someStringB))
print("({valueA} < {valueB}): {result}" .format(valueA = someStringA, valueB = someStringB, result = someStringA < someStringB))
print("({valueA} <= {valueB}): {result}".format(valueA = someStringA, valueB = someStringB, result = someStringA <= someStringB))
print("({valueA} == {valueB}): {result}".format(valueA = someStringA, valueB = someStringB, result = someStringA == someStringB))
print("({valueA} != {valueB}): {result}".format(valueA = someStringA, valueB = someStringB, result = someStringA != someStringB))

print("\n* — с объектами типа String (str) возможно производить те же операции, что и с объектами типа Numbers (int, float, ...).")

print("\nИндексация строк:")
print("Вывод 1 символ объекта someStringA: {result}"                    .format(result = someStringA[0]))
print("Вывод с 1 по 4 символ объекта someStringA: {result}"             .format(result = someStringA[0:4]))
print("Вывод символов объекта someStringA через 1: {result}"            .format(result = someStringA[::2]))
print("Вывод символов объекта someStringA в обратном порядке: {result}" .format(result = someStringA[::-1]))

print("\nКодирование / Декодирование:")
some_string_c = 'йцукен'.encode()
print("Строка: {value}, была закодирована и декодирована (Кодировка: по умолчанию (UTF-8.)). Результат: {result}".format(value = some_string_c, result = some_string_c.decode()))