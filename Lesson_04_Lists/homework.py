# ПАМЯТКА: Списки (Lists)
# Создание: my_list = [1, 2, "three"]
# Индексация: my_list[0] (первый), my_list[-1] (последний)
# Срезы: my_list[start:end:step] (например, [1:3])
# Методы:
#   .append(x) - добавить в конец
#   .insert(i, x) - вставить по индексу
#   .pop(i) - удалить и вернуть (по умолчанию последний)
#   .remove(x) - удалить первое вхождение x
#   .sort() - сортировать
# len(my_list) - длина списка
# x in my_list - проверка наличия

# Домашнее задание: Списки (AQA Focus)

# 1. Список тестовых сценариев:
# Создайте список `test_cases`, содержащий 5 названий тестов (строки).
# Ваш код:

test_cases = ["Проверка того то", "Проверка сего то", "Проверка там та", "Проверка сям та", "Проверка туда сюда"]
print(test_cases)

# 2. Добавление теста (setup):
# Добавьте в конец списка `test_cases` новый тест "Logout test".
# Ваш код:

test_cases.append("Logout test")
print(test_cases)


# 3. Приоритизация (insert):
# Вставьте "Critical: UI Login" на вторую позицию (индекс 1) в списке.
# Ваш код:

test_cases.insert(1, "Critical: UI Login")
print(test_cases)

# 4. Удаление пройденного теста:
# Удалите первый тест из списка (предположим, он уже прошел).
# Ваш код:

test_cases.remove("Проверка того то")
print(test_cases)

# 5. Последний выполненный тест:
# Выведите последний элемент списка, используя отрицательный индекс.
# Ваш код:

print(test_cases[-1])

# 6. Срезы (Smoke tests):
# Создайте новый список `smoke_tests`, взяв первые 3 элемента из `test_cases`.
# Ваш код:

smoke_tests = test_cases[:3]
print(smoke_tests)

# 7. Время выполнения (sum):
# Дан список времени выполнения тестов: timings = [1.2, 0.5, 2.3, 1.0, 0.8].
# Выведите общее время выполнения всех тестов.
# Ваш код:

timings = [1.2, 0.5, 2.3, 1.0, 0.8]


print(sum(timings))


# 8. Сортировка по времени:
# Отсортируйте список `timings` от меньшего к большему.
# Ваш код:
print(sorted(timings))

# 9. List Comprehension (Фильтрация результатов):
# Дан список результатов: results = ["PASSED", "FAILED", "PASSED", "PASSED", "FAILED"].
# Создайте новый список `failed_only`, содержащий только элементы "FAILED".
# Ваш код:


results = ["PASSED", "FAILED", "PASSED", "PASSED", "FAILED"]
failed_only = list(filter(lambda result: result == "FAILED", results))
print(failed_only)

# 10. Подсчет падений:
# Посчитайте количество "FAILED" в списке `results`.
# Ваш код:

results = ["PASSED", "FAILED", "PASSED", "PASSED", "FAILED"]
failed_only = list(filter(lambda result: result == "FAILED", results))
print(len(failed_only))


# 11. Поиск индекса:
# Найдите индекс первого элемента "FAILED" в списке `results`.
# Ваш код:

results = ["FAILED","PASSED", "FAILED", "PASSED", "PASSED", "FAILED"]
index = results.index("PASSED")
print(index)

# 12. Разворот очереди (reverse):
# Разверните список `test_cases` задом наперед, чтобы последние тесты стали первыми.
# Ваш код:

test_cases = ["Проверка того то", "Проверка сего то", "Проверка там та", "Проверка сям та", "Проверка туда сюда"]
print(list(reversed(test_cases)))

# 13. Deep Copy (Важно для тестов):
# Создайте независимую копию списка `test_cases`. Измените в ней один элемент.
# Проверьте, что оригинал остался прежним.
# Ваш код:

test_cases = ["Проверка того то", "Проверка сего то", "Проверка там та", "Проверка сям та", "Проверка туда сюда"]
copy_cases = list(test_cases)
copy_cases.insert(2, "Logout")
print(copy_cases)


# 14. Очистка (teardown):
# Удалите все элементы из списка `smoke_tests`.
# Ваш код:

smoke_tests.clear()
print(smoke_tests)

# 15. Объединение наборов (extend/+):
# Объедините два списка: web_tests = ["t1", "t2"] и api_tests = ["t3", "t4"].
# Ваш код:

web_tests = ["t1", "t2"]
api_tests = ["t3", "t4"]
web_tests.extend(api_tests)
print(web_tests)

# 16. Удаление по значению:
# Удалите конкретный тест "Logout test" из списка по его названию.
# Ваш код:

test_cases = ["Проверка того то", "Проверка сего то", "Проверка там та", "Проверка сям та", "Проверка туда сюда", "Logout test"]
test_cases.remove("Logout test")
print(test_cases)

# 17. Преобразование лога (split):
# Дана строка лога: "2023-10-01|LOGIN|SUCCESS".
# Разделите её по символу "|", чтобы получить список частей.
# Ваш код:

logy = "2023-10-01|LOGIN|SUCCESS"
parts = logy.split("|")
print(parts)

# 18. Форматирование отчета (join):
# Превратите список `['Step 1', 'Step 2', 'Step 3']` в строку, разделенную стрелочками " -> ".
# Ваш код:

join_list = " -> ".join(['Step 1', 'Step 2', 'Step 3'])
print(join_list)

# 19. Граничные значения:
# Найдите самый быстрый (min) и самый медленный (max) тест в списке `timings`.
# Ваш код:

timings = [1.2, 0.5, 2.3, 1.0, 0.8]
minimal_test = min(timings)
maximum_test = max(timings)
print(minimal_test, maximum_test)

# 20. Уникальные ошибки (set):
# Дан список имен найденных багов (могут дублироваться).
# Получите список уникальных имен багов.
# bugs = ["UI error", "API slow", "UI error", "DB error"]
# Ваш код:


bugs = ["UI error", "API slow", "UI error", "DB error"]
uniqal_bugs = list(set(bugs))
print(uniqal_bugs)