some_value_a = 5
some_value_b = 25
some_list = [1, 2, 3, 4, 5]

print("Арифметические операторы:")
print("Добавление: {value_a} + {value_b} = {result}".format(value_a = some_value_a, value_b = some_value_b, result = some_value_a + some_value_b))
print("Вычитание: {value_a} - {value_b} = {result}" .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a - some_value_b))
print("Умножение: {value_a} * {value_b} = {result}" .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a * some_value_b))
print("Деление: {value_a} / {value_b} = {result}"   .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a / some_value_b))
print("Модуль (нечетное значение): 5 % 2 = {result}".format(result = 5 % 2))
print("Модуль (четное значение): 4 % 2 = {result}"  .format(result = 4 % 2))
print("Степень: {value_a} ** {value_b} = {result}"  .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a ** some_value_b))
print("Деление с остатком: 3 // 2 = {result}"       .format(result = 3 // 2))
print("* — операторы присваивания работают аналогичным образом.")

print("\nОператоры сравнения:")
print("({value_a} > {value_b}): {result}" .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a > some_value_b))
print("({value_a} >= {value_b}): {result}".format(value_a = some_value_a, value_b = some_value_b, result = some_value_a >= some_value_b))
print("({value_a} < {value_b}): {result}" .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a < some_value_b))
print("({value_a} <= {value_b}): {result}".format(value_a = some_value_a, value_b = some_value_b, result = some_value_a <= some_value_b))
print("({value_a} == {value_b}): {result}".format(value_a = some_value_a, value_b = some_value_b, result = some_value_a == some_value_b))
print("({value_a} != {value_b}): {result}".format(value_a = some_value_a, value_b = some_value_b, result = some_value_a != some_value_b))

print("\nЛогические операторы:")
print("({value_a} > {value_b} and {value_a} < {value_b}): {result}" .format(value_a = some_value_a, value_b = some_value_b, 
                                                                result = some_value_a > some_value_b and some_value_a < some_value_b))
print("(not ({value_a} > {value_b} and {value_a} < {value_b})): {result}" .format(value_a = some_value_a, value_b = some_value_b, 
                                                                result = not (some_value_a > some_value_b and some_value_a < some_value_b)))
print("({value_a} > {value_b} or {value_a} < {value_b}): {result}"  .format(value_a = some_value_a, value_b = some_value_b, 
                                                                result = some_value_a > some_value_b or some_value_a < some_value_b))
                                                                
print("\nОператоры членства:")
print("({value_a} in {list}): {result}"      .format(value_a = some_value_a, list = some_list, result = some_value_a in some_list))
print("({value_a} not in {list}): {result}"  .format(value_a = some_value_a, list = some_list, result = some_value_a not in some_list))

print("\nОператоры идентификации:")
print("({value_a} is {value_b}): {result}"        .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a is some_value_b))
print("({value_a} is not {value_b}): {result}"    .format(value_a = some_value_a, value_b = some_value_b, result = some_value_a is not some_value_b))

print("Пример: 2 + 2 =", 2 + 2)