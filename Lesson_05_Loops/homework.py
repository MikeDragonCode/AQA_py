# ПАМЯТКА: Циклы (Loops)
# for item in sequence:
#     # выполняем код для каждого элемента
#
# range(5) -> 0, 1, 2, 3, 4
#
# while condition:
#     # выполняем пока условие True
#
# break - прервать цикл
# continue - перейти к следующей итерации
#
# enumerate(list) - возвращает пары (index, value)

# Домашнее задание: Циклы (AQA Focus)

# 1. Запуск набора тестов:
# Пройдитесь циклом по списку `['test_login', 'test_signup', 'test_profile']`.
# Для каждого теста выведите "Executing {name}...".
# Ваш код:

test_nabor =['test_login', 'test_signup', 'test_profile']
for i in test_nabor:
    var = "Executing " + i
    print(var)

# 2. Ожидание элемента (while):
# Напишите цикл while, который имитирует ожидание элемента.
# Есть переменная `element_found = False` и `attempts = 0`.
# Цикл должен работать, пока элемент не найден И попыток меньше 5.
# Каждую итерацию выводите "Attempt {attempts}: Waiting for element...".
# В конце каждой итерации увеличивайте attempts на 1. 
# На 3-й попытке установите `element_found = True`.
# Ваш код:

element_found = False
attempts = 0

while not element_found and attempts < 5:
    print("Attempt {attempts}: Waiting for element...")
    attempts += 1
    
    if attempts == 3:
        element_found = True

print("Element found!" if element_found else "Element not found after 5 attempts.")


# 3. Приветствие пользователей:
# Дан список пользователей для тестов: ["Admin", "User1", "User2"].
# Выведите приветствие для каждого.
# Ваш код:
pol = ["Admin", "User1", "User2"]
for i in pol:
    var = "Hello " + i
    print(var)

# 4. Общая длительность тестов:
# Дан список времени: [2, 5, 1, 4]. Посчитайте сумму всех чисел через цикл for.
# Ваш код:

time = [2, 5, 1, 4]
sum = 0
for i in time:
    sum =sum + i
print(sum)

# 5. Поиск критического бага:
# В списке `['low', 'medium', 'critical', 'high']` найдите 'critical' через цикл.
# Если нашли - выведите "Found it!" и ПРЕРВИТЕ цикл (break).
# Ваш код:

bugs = ['low', 'medium', 'critical', 'high']
for i in bugs:
    if "critical" in bugs:
        print("Found it!")
        break

# 6. Пропуск неактивных тестов (continue):
# Дан список: `[('t1', True), ('t2', False), ('t3', True)]` (название, включен ли).
# Распечатайте только названия включенных (True) тестов.
# Ваш код:

tests = [('t1', True), ('t2', False), ('t3', True)]

for test_name, is_active in tests:
    if not is_active:
        continue
    print(test_name)


# 7. Таблица параметров (вложенные циклы):
# У вас есть список браузеров `['chrome', 'firefox']` и список URL `['google.com', 'yandex.ru']`.
# Распечатайте все пары запуска: "Testing {url} on {browser}".
# Ваш код:

browser = ['chrome', 'firefox']
url = ['google.com', 'yandex.ru']
for i in browser:
    for j in url:
        print(f"Testing {j} on {i}")

# 8. Итерация по буквам:
# Проверьте, есть ли цифра в строке "token_123", используя цикл for.
# Ваш код:

var = "token_123"
var2 = any(char.isdigit()for char in var)
print(var2)

# 9. Построчный отчет (итерация по словарю):
# Даны результаты тестов: `{'login': 'passed', 'logout': 'failed'}`.
# Выведите "Test {name} status is {status}".
# Ваш код:

test = {'login': 'passed', 'logout': 'failed'}
for test_name, status in test.items():
    print(f"Test {test_name} status is {status}")


# 10. Пронумерованные шаги (enumerate):
# Дан список шагов: `['Open page', 'Enter login', 'Submit']`.
# Выведите: "Step 1: Open page", "Step 2: Enter login" и т.д.
# Ваш код:
steps = ['Open page', 'Enter login', 'Submit']
for index, znach in enumerate(steps, start=1):
    print(f"Step {index}: {znach}")

# 11. Проверка на пустые результаты (else в цикле):
# Проверьте список результатов на наличие слова "ERROR".
# Если нашли - "System failure!", если цикл прошел до конца и ERROR не было - "System stable".
# Ваш код:


results = ['OK', 'OK', 'ERROR', 'OK']
error_found = False

for i in results:
    if i == 'ERROR':
        error_found = True 
        break  


if error_found:
    print("System failure!")  
else:
    print("System stable")  


# 12. Обратный отсчет до тайм-аута:
# Реализуйте обратный отсчет от 5 до 1 с помощью while.
# Ваш код:

i = 5
while i >= 1:
    print(i)
    i = i - 1
    

# 13. Генератор тестовых id:
# Создайте список id тестов от "id_0" до "id_10", используя list comprehension.
# Ваш код:


test_ids = [f"id_{i}" for i in range(11)]
print(test_ids)


# 14. Сборка пар (zip):
# Даны списки тестов и их статусов. Соберите их в пары и выведите "Test: Status".
# tests = ['t1', 't2'], statuses = ['ok', 'error']
# Ваш код:

# Списки тестов и их статусов
tests = ['t1', 't2']
statuses = ['ok', 'error']

for i in range(len(tests)):
    print(f"{tests[i]}: {statuses[i]}")


# 15. Фильтрация медленных тестов:
# Дан список timings = [0.1, 2.5, 0.3, 4.0, 0.2].
# Выведите только те, которые длятся более 1 секунды.
# Ваш код:


timings = [0.1, 2.5, 0.3, 4.0, 0.2]


long_timings = [time for time in timings if time > 1]
print(long_timings)
