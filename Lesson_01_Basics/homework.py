# ПАМЯТКА: Основы Python
# Переменные: name = "Tom", age = 22
# Типы данных:
#   int (целые): 1, 10, -5
#   float (дробные): 3.14, 0.5
#   str (строки): "Hello", 'World'
#   bool (булево): True, False
# print(x) - вывод на экран
# input("Enter: ") - ввод с клавиатуры (всегда возвращает строку!)
# int("10") - преобразование строки в число
# f"Hello, {name}" - f-строка (вставка переменных)

# Домашнее задание: Основы Python (AQA Start)

# 1. Типы данных в тестировании:
# Создайте переменные для хранения результатов теста:
#   test_name (строка) - название теста, например "Login Check"
#   execution_time (float) - время выполнения, например 0.5
#   is_passed (bool) - статус прохождения, True или False
# Выведите их типы с помощью print(type(...)).
# Ваш код:

#test_name = input()
#execution_time = float(input())
#is_passed = bool(input())
#print(type(test_name))
#print(type(execution_time))
#print(type(is_passed))

# 2. Форматирование отчета (f-strings):
# Используя переменные из задания 1, выведите строку ровно в таком формате:
# "Test: Login Check | Status: PASSED | Time: 0.5s"
# (Вместо PASSED/FAILED подставьте значение is_passed, пока просто текстом или str(is_passed))
# Ваш код:

# print('Тест : ' + test_name + ' | ' + 'Status : ' + str(is_passed) + ' | ' + 'Time : ' + str(execution_time))

# 3. Работа с URL (строки):
# Дана переменная base_url = "https://example.com"
# Дана переменная endpoint = "/api/v1/users"
# Склейте их в полный URL и выведите на экран.
# Ваш код:
base_url = "https://example.com"
endpoint = "/api/v1/users"
print( base_url + endpoint)

# 4. Преобразование полученных данных:
# Представьте, что API вернул вам количество пользователей в виде строки "500".
# Создайте переменную users_count_str = "500".
# Преобразуйте её в целое число (int), прибавьте 1 (создали нового юзера) и выведите результат.
# Ваш код:
users_count_str = "500"
print(int(users_count_str) + 1)

# 5. Математические операции с таймаутами:
# Вы ждете элемент 10 секунд (total_timeout = 10).
# Проверка происходит каждые 2 секунды (poll_interval = 2).
# Посчитайте, сколько раз произойдет проверка (количество попыток).
# Ваш код:
total_timeout = 10
poll_interval = 2
print(total_timeout // poll_interval)

# 6. Округление времени:
# Тест шел 3.1415926 секунды.
# Округлите это значение до 2 знаков после запятой для отчета.
# Ваш код:
time_test = 3.1415926
rounded_value = round(time_test, 2)
print(rounded_value)

# 7. Длина токена:
# Вам пришел токен авторизации "abcdef12345".
# Проверьте (выведите) его длину.
# Ваш код:
# Токен авторизации
token = "abcdef12345"
token_length = len(token)
print(token_length)

# 8. Множественное присваивание (setup/teardown):
# В одной строке инициализируйте переменные для размеров окна браузера:
# width = 1920, height = 1080. Выведите их.
# Ваш код:
width, height = 1920, 1080
print(width, height)

# 9. Обмен данными (фикстуры):
# Есть переменная current_user = "Admin".
# Есть переменная new_user = "Guest".
# Поменяйте их значения местами, чтобы current_user стал "Guest".
# Ваш код:

current_user = "Admin"
new_user = "Guest"
var = "Guest"
current_user = new_user
new_user = var
print(current_user)

# 10. Логические проверки (Assert preparation):
# Проверьте, правда ли, что status_code (создайте переменную = 200) равен 200,
# И при этом response_time (создайте = 0.5) меньше 1.0.
# Выведите результат (True/False).
# Ваш код:
status_code = 200
response_time = 0.5
if status_code == 200 and response_time < 1.0:
    print("True")
else:
    print("False")