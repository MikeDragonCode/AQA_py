# ПАМЯТКА: Функции
# Определение: 
#   def my_func(arg1: int, arg2: str = "default") -> bool:
#       # тело функции
#       return True
#
# Type Hints (Подсказки типов): : int, : str, -> bool/None/int
#
# *args - список позиционных аргументов
# **kwargs - словарь именованных аргументов

# Домашнее задание: Функции (AQA Focus)

# 1. Простая функция валидации:
# Напишите функцию `check_status`, которая принимает `status_code` (int).
# Она должна выводить "Success" если код 200, и "Error" в остальных случаях.
# (Пока без возврата значения, только print).
# Ваш код:

def check_status(status_code):
    if status_code == 200:
        return 'Success'
    else:
        return 'Error'

res = check_status(400)
print(res)

# 2. Функция с возвратом значения и типами:
# Напишите функцию `get_full_url`, которая принимает `base_url` (str) и `path` (str).
# Функция должна возвращать (return) полный URL (склеенную строку).
# Добавьте аннотации типов (type hints) для аргументов и возвращаемого значения.
# Ваш код:

def get_full_url(base_url: str, path: str):
    res = base_url + path
    return res

base_url = "www.baobab.ru"
path = "/jsdjkdsjk/dskjdsjkds"
endpoint = get_full_url(base_url, path)
print(type(endpoint), endpoint)
print(type(base_url), type(path))


# 3. Аргументы по умолчанию:
# Напишите функцию `click_element`, которая принимает `locator` (str) и `timeout` (int).
# Сделайте так, чтобы `timeout` по умолчанию был равен 5.
# Функция должна выводить "Clicking on {locator} with timeout {timeout}".
# Ваш код:


def click_element(locator: str, timeout ):
    print('Clicking on', locator, 'with timeout', timeout )
click_element('locator',5)


# 4. Вспомогательная функция (Assert Helper):
# Напишите функцию `assert_equals`, которая принимает `actual` (любой тип) и `expected` (любой тип).
# Если они равны - выводит "Test PASSED".
# Если не равны - выводит "Test FAILED: expected {expected}, got {actual}".
# Ваш код:

def assert_equals(actual, expected):
    if actual == expected:
        return "Test PASSED"
    else:
        return "Test FAILED"

res = assert_equals('250', '250')
print(res)


# 5. Именованные аргументы:
# Напишите функцию `create_user`, которая принимает `name`, `email` и `age`.
# Вызовите её, передав аргументы в другом порядке, используя их имена (например, сначала age, потом name).
# Ваш код:

def create_user(name, email, age):
    print(age, name, email)
create_user(age=30, name='Philipp', email='vrubelfilipp@gmail.com')

# 6. *args для логирования:
# Напишите функцию `log_steps`, которая принимает произвольное количество строк (*args) - шагов теста.
# Функция должна выводить каждый шаг с префиксом "Step: ".
# Ваш код:

def log_steps(*args):
    for step in args:
        print("Step:", step)

log_steps("Начать тест", "Проверить входные данные", "Сохранить результаты", "Завершить тест")



# 7. **kwargs для конфигурации:
# Напишите функцию `connect_to_db`, которая принимает произвольные параметры подключения (**kwargs).
# Выведите параметры подключения в виде пар "Key: Value".
# Пример вызова: connect_to_db(host="localhost", port=5432, user="admin")
# Ваш код:

def connect_to_db(**kwargs):
     for key, value in kwargs.items():
          print(f"{key}: {value}")
connect_to_db(host="localhost", port=5432, user="admin")

# 8. Фильтрация (функция-предикат):
# Напишите функцию `is_visible`, которая принимает строку (например, "visible" или "hidden")
# и возвращает True, если строка равна "visible".
# Используйте типизацию `-> bool`.
# Ваш код:

def is_visible(visible: str):
    if visible == 'visible':
        return visible
res = bool(is_visible('viible'))
print(res)

# 9. Docstring (Документирование):
# Добавьте к функции `assert_equals` (из задания 4) строку документации,
# описывающую, что делает функция.
# Ваш код:

def assert_equals(actual, expected):
    """
    Проверяет, равны ли два значения.

    Параметры:
    actual: Значение, которое было получено (фактическое).
    expected: Значение, которое ожидалось.

    Возвращает:
    str: "Test PASSED", если значения равны, иначе "Test FAILED".
    """
    if actual == expected:
        return "Test PASSED"
    else:
        return "Test FAILED"

res = assert_equals('250', '250')
print(res)


# 10. Lambda для сортировки:
# Есть список ответов API (числа - время отклика): timings = [0.5, 0.1, 1.2, 0.3].
# Используйте sorted() с lambda, чтобы отсортировать их (хотя для чисел lambda не обязательна,
# представьте, что это словари, но здесь просто потренируйтесь на синтаксисе lambda x: ...).
# Или напишите лямбду, которая проверяет, что число меньше 1.0.
# Ваш код:


timings = [0.5, 0.1, 1.2, 0.3]

sorted_time = sorted(timings, key=lambda x: x)
print(sorted_time)
