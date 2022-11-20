someValueA = 5
someValueB = 25
someList = [1, 2, 3, 4, 5]

print("Арифметические операторы:")
print("Добавление: {valueA} + {valueB} = {result}"  .format(valueA = someValueA, valueB = someValueB, result = someValueA + someValueB))
print("Вычитание: {valueA} - {valueB} = {result}"   .format(valueA = someValueA, valueB = someValueB, result = someValueA - someValueB))
print("Умножение: {valueA} * {valueB} = {result}"   .format(valueA = someValueA, valueB = someValueB, result = someValueA * someValueB))
print("Деление: {valueA} / {valueB} = {result}"     .format(valueA = someValueA, valueB = someValueB, result = someValueA / someValueB))
print("Модуль (нечетное значение): 5 % 2 = {result}".format(result = 5 % 2))
print("Модуль (четное значение): 4 % 2 = {result}"  .format(result = 4 % 2))
print("Степень: {valueA} ** {valueB} = {result}"    .format(valueA = someValueA, valueB = someValueB, result = someValueA ** someValueB))
print("Деление с остатком: 3 // 2 = {result}"       .format(result = 3 // 2))
print("* — операторы присваивания работают аналогичным образом.")

print("\nОператоры сравнения:")
print("({valueA} > {valueB}): {result}" .format(valueA = someValueA, valueB = someValueB, result = someValueA > someValueB))
print("({valueA} >= {valueB}): {result}".format(valueA = someValueA, valueB = someValueB, result = someValueA >= someValueB))
print("({valueA} < {valueB}): {result}" .format(valueA = someValueA, valueB = someValueB, result = someValueA < someValueB))
print("({valueA} <= {valueB}): {result}".format(valueA = someValueA, valueB = someValueB, result = someValueA <= someValueB))
print("({valueA} == {valueB}): {result}".format(valueA = someValueA, valueB = someValueB, result = someValueA == someValueB))
print("({valueA} != {valueB}): {result}".format(valueA = someValueA, valueB = someValueB, result = someValueA != someValueB))

print("\nЛогические операторы:")
print("({valueA} > {valueB} and {valueA} < {valueB}): {result}" .format(valueA = someValueA, valueB = someValueB, 
                                                                result = someValueA > someValueB and someValueA < someValueB))
print("(not ({valueA} > {valueB} and {valueA} < {valueB})): {result}" .format(valueA = someValueA, valueB = someValueB, 
                                                                result = not (someValueA > someValueB and someValueA < someValueB)))
print("({valueA} > {valueB} or {valueA} < {valueB}): {result}" .format(valueA = someValueA, valueB = someValueB, 
                                                                result = someValueA > someValueB or someValueA < someValueB))
                                                                
print("\nОператоры членства:")
print("({valueA} in {list}): {result}"      .format(valueA = someValueA, list = someList, result = someValueA in someList))
print("({valueA} not in {list}): {result}"  .format(valueA = someValueA, list = someList, result = someValueA not in someList))

print("\nОператоры идентификации:")
print("({valueA} is {valueB}): {result}"        .format(valueA = someValueA, valueB = someValueB, result = someValueA is someValueB))
print("({valueA} is not {valueB}): {result}"    .format(valueA = someValueA, valueB = someValueB, result = someValueA is not someValueB))