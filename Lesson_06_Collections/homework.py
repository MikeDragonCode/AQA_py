# ПАМЯТКА: Коллекции
# Словари (dict): 
#   my_dict = {'id': 1, 'name': 'test'}
#   my_dict['id'] -> 1
#   my_dict.get('key', default) -> безопасный способ
#   .items() -> [(k, v), ...]
#
# Множества (set):
#   {1, 2, 3} (только уникальные)
#   & (пересечение), | (объединение)

# Домашнее задание: Коллекции (AQA Focus - Работа с JSON/API)
import random
import string

# 1. Модель пользователя:
# Создайте словарь `user_data`, представляющий ответ от API.
# Поля: 'id', 'username', 'email', 'status' (например, 'active').
# Ваш код:

user_data = {'id': 2, 'username': 'test', 'email': 'vrv@gmail.com', 'status': 'active'}
print(user_data)


# 2. Проверка значения:
# Выведите значение 'email' из словаря `user_data`.
# Ваш код:

print(user_data['email'])

# 3. Обновление статуса:
# Измените 'status' на 'suspended' в словаре.
# Ваш код:

user_data['status'] = 'suspended'
print(user_data)

# 4. Добавление данных (Token):
# Добавьте новый ключ 'token' со случайной строкой в словарь.
# Ваш код:

result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
user_data['token'] = result
print(user_data)

# 5. Безопасное получение ключа (get):
# Попробуйте достать ключ 'last_login'. Если его нет - выведите "Never".
# Ваш код:

pr = user_data.get('last_login')
if pr == None:
    print("Never")


# 6. Состав ответа (Keys/Values):
# Выведите список всех ключей, которые вернул API в `user_data`.
# Ваш код:
user_data = {'id': 2, 'username': 'test', 'email': 'vrv@gmail.com', 'status': 'active'}
key = list(user_data.keys())
print(key)


# 7. Динамические заголовки:
# Установите заголовок 'Content-Type' в 'application/json', используя setdefault.
# headers = {'Authorization': 'Bearer 123'}
# Ваш код:
headers = {'Authorization': 'Bearer 123'}
headers.setdefault('Content-Type', 'application/json')
print(headers)


# 8. Набор ролей (Sets):
# Создайте множество `required_permissions`: {'read', 'write', 'delete'}.
# Ваш код:
slov = {'read', 'write', 'delete'}
required_permissions = set(slov)
print(required_permissions)

# 9. Проверка прав:
# У пользователя есть права `user_permissions`: {'read', 'write'}.
# Добавьте ему право 'execute'.
# Ваш код:
user_permissions = {'read', 'write'}
user_permissions.add('execute')
print(user_permissions)

# 10. Дубликаты в логах:
# Пришел список id событий: [101, 102, 101, 103, 102].
# Очистите его от дубликатов с помощью множества.
# Ваш код:

spisok = [101, 102, 101, 103, 102]
print(set(spisok))

# 11. Пересечение (Общие баги):
# Есть баги в Chrome: {'b1', 'b2', 'b3'} и баги в Firefox: {'b2', 'b3', 'b4'}.
# Найдите баги, которые воспроизводятся в ОБОИХ браузерах.
# Ваш код:
Chrome = {'b1', 'b2', 'b3'}
Firefox = {'b2', 'b3', 'b4'}
print(Chrome.intersection(Firefox))

# 12. Разница (Уникальные ошибки):
# Найдите баги, которые есть только в Chrome, но которых нет в Firefox.
# Ваш код:
Chrome = {'b1', 'b2', 'b3'}
Firefox = {'b2', 'b3', 'b4'}
print(Chrome.difference(Firefox))


# 13. Неизменяемый конфиг (Tuples):
# Создайте кортеж `db_config` с параметрами (host, port, user).
# Попробуйте изменить порт (убедитесь, что это невозможно).
# Ваш код:
db_config = ('host', 'port', 'user')



# 14. Распаковка ответа:
# Пришел кортеж с результатом теста: `result = ("test_login", "PASSED", 0.5)`.
# Распакуйте его в переменные name, status, duration.
# Ваш код:
result = ("test_login", "PASSED", 0.5)
name, status, duration = result
print(name)     
print(status)   
print(duration) 


# 15. Вложенный JSON (Сложный объект):
# Создайте словарь `response`, где внутри ключа 'data' лежит список из двух словарей (двух пользователей).
# Достаньте имя второго пользователя.
# Ваш код:

response = {'data':[{'guest_1':'Fil',},{'guest_2':'Andrey'}]}
print(response)

# 16. Проверка наличия ключей:
# Дан список `required_fields = ['id', 'name', 'email']`.
# Проверьте, все ли эти поля есть в словаре `user_data`.
# Ваш код:
required_fields = ['id', 'name', 'email']
result = all(item in user_data.values() for item in required_fields)
print(result)

# 17. Конвертация для отчета:
# Превратите список кортежей `[('id', 1), ('name', 'Alex')]` в словарь.
# Ваш код:
data_tuples = [('id', 1), ('name', 'Alex')]
data_dict = dict(data_tuples)

# 18. Дефолтные настройки:
# Создайте словарь с конфигурацией, объединив два словаря: 
# default_config = {'timeout': 30, 'browser': 'chrome'}
# user_config = {'browser': 'firefox'}
# (user_config должен переопределять значения из default_config).
# Ваш код:

default_config = {'timeout': 30, 'browser': 'chrome'}
user_config = {'browser': 'firefox'}
final_config = default_config.copy()  
final_config.update(user_config)       
print(final_config)  
