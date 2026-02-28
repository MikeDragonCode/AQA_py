# ПАМЯТКА: Модули и пакеты
# import module_name
# from module_name import function_name
# import module_name as alias (псевдоним)
#
# Стандартные модули для AQA:
#   math - математика
#   random - генерация данных (имена, почты)
#   datetime - работа с таймштампами отчетов
#   os, sys - работа с путями и окружением
#   json, csv - работа с данными

# Домашнее задание: Модули и пакеты (AQA Focus - Инструментарий)

# 1. Использование собственного инструментария:
# Импортируйте функции `add` и `subtract` из модуля `math_utils.py` (который лежит рядом).
# Сложите время выполнения двух тестов (0.5 и 1.2) и выведите результат.
# Ваш код:

from mod import math_utils
print(math_utils.add(0.5, 1.2)) 

# 2. Использование псевдонима:
# Импортируйте модуль `math_utils` как `qa_math`. Вызовите функцию вычитания.
# Ваш код:
print(math_utils.subtract(1.2, 0.5))

# 3. Генерация тестовых данных (Random):
# Сгенерируйте случайную строку для имени пользователя (например, "user_74").
# Число должно быть в диапазоне от 1 до 100.
import random
import string
# Ваш код:
random_str = ''.join(random.choices(string.ascii_letters, k=10))
random_int = random.randint(0, 100)
print(random_str + "_" + str(random_int))

# 4. Выбор случайного элемента:
# Есть список браузеров: browsers = ['chrome', 'firefox', 'safari', 'edge'].
# Выберите случайный браузер для запуска теста.
# Ваш код:
browsers = ['chrome', 'firefox', 'safari', 'edge']
list_ran = random.choice(browsers)
print(str(list_ran))

# 5. Временные метки (Datetime):
# Получите текущую дату и время для названия отчета.
# Выведите дату в формате ГГГГ-ММ-ДД.
from datetime import datetime
# Ваш код:
data = datetime.now()
print(data)
# 6. Математика в тестах:
# Вам нужно вычислить площадь элемента. Дан радиус r = 10.
# Используйте math.pi.
import math
r = 10
# Ваш код:
S = math.pow((math.pi * r), 2)
print(S)

# 7. Работа с переменными окружения (OS):
# Получите список всех файлов в текущей папке проекта (os.listdir).
import os
# Ваш код:



current_directory = os.getcwd()
files_and_folders = os.listdir(current_directory)
files = [f for f in files_and_folders if os.path.isfile(os.path.join(current_directory, f))]
print(files)


# 8. Параметры командной строки (Sys):
# Выведите список аргументов, с которыми был запущен скрипт (sys.argv).
# (Это часто используется для передачи параметров запуска тестов, например: --browser chrome)
import sys

for index, arg in enumerate(sys.argv):
    print(f"Аргумент {index}: {arg}")




# 9. Работа с JSON (Симуляция API):
# Дан словарь-запрос: payload = {'id': 1, 'name': 'test'}.
# Преобразуйте его в JSON-строку.
import json
# Ваш код:
payload = {'id': 1, 'name': 'test'}
print(json.dumps(payload))

# 10. Проверка __name__ == "__main__":
# Опишите в комментариях, зачем мы используем конструкцию if __name__ == "__main__": 
# при написании модулей с тестами/фикстурами.
# Ваш код:
#для определения того, выполняется ли модуль как основная программа или импортируется в качестве модуля в другой файл. 