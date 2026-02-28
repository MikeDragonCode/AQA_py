# ПАМЯТКА: Работа с файлами
# with open('file.txt', 'mode') as f:
#     # работаем с файлом 
#
# Режимы (mode):
#   'r' - чтение (read)
#   'w' - запись (write), затирает файл!
#   'a' - дозапись (append), добавляет в конец
#
# Методы:
#   content = f.read() - читать весь файл
#   lines = f.readlines() - читать список строк
#   f.write("text") - записать строку

# Домашнее задание: Работа с файлами (AQA Focus - Логи и конфиги)

# 1. Запись тест-кейса:
# Создайте файл 'test_report.txt' и запишите в него строку "Test Login: PASSED".
# Ваш код:

with open('test_report.txt', 'w') as file:
    file.write("Test Login: PASSED")
file.close()


with open('test_report.txt', 'w') as file:
    file.write("Test Login: PASSED")


# 2. Чтение логов:
# Прочитайте содержимое 'test_report.txt' и выведите его на экран.
# Ваш код:
with open('test_report.txt', 'r') as file:
    content = file.read()
print(content)


# 3. Добавление шагов в лог:
# Откройте тот же файл в режиме дозаписи ('a') и добавьте новую строку:
# "Step 1: Open Home Page\nStep 2: Enter Credentials".
# Ваш код:
with open('test_report.txt', 'a') as file:
   file.write("\nStep 1: Open Home Page\nStep 2: Enter Credentials")

# 4. Анализ списка тестов:
# Считайте файл и сохраните его строки в список. Выведите количество строк в файле.
# Ваш код:
#with open('test_report.txt', 'r') as file:
#   content = file.read()
#spisok = (list(content))
#print(spisok, len(spisok))

# 5. Экспорт тестовых данных:
# Дан список словарей с тестовыми данными: 
# data = [{'user': 'admin', 'pass': '123'}, {'user': 'guest', 'pass': 'qwerty'}]
# Запишите каждое имя пользователя в новый файл 'users.txt' (каждое с новой строки).
# Ваш код:
#data = [{'user': 'admin', 'pass': '123'}, {'user': 'guest', 'pass': 'qwerty'}]
#with open('users.txt', 'w') as file:
#    for i in data:
#        file.write(i['user'] + '\n')
    

# 6. Поиск ошибок в логе (Парсинг):
# Создайте файл 'server.log' со строками:
# "INFO: Server started"
# "EtRROR: Connection failed"
# "INFO: Retry atempt 1"
# "ERROR: Timeout reached"
# Прочитайте этот файл и выведите в консоль ТОЛЬКО строки, содержащие "ERROR".
# Ваш код:
with open('server.log', 'w') as file:
    file.write("INFO: Server started\nERROR: Connection failed\nINFO: Retry attempt 1\nERROR: Timeout reached")
with open('server.log', 'r') as file:
    for i in file:
        if "ERROR" in i:
            print(i.strip())






# 7. Работа с кодировкой (Кириллица):
# Запишите строку "Отчет по тестированию" в файл 'report_ru.txt' с кодировкой utf-8.
# Затем прочитайте её.
# Ваш код:

with open('report_ru.txt', 'w', encoding='utf-8') as file:
    file.write('Отчет по тестированию')
with open('report_ru.txt', 'r', encoding='utf-8') as file:
    content = file.read()
print(content)

# 8. Редактирование конфига (r+):
# Откройте файл 'test_report.txt' в режиме 'r+'.
# Считайте первую строку, затем переместитесь в начало (seek(0)) и замените "PASSED" на "FAILED".
# Ваш код:
# Открываем файл 'test_report.txt' в режиме 'r+'.

with open('test_report.txt', 'r+') as file:
    content = file.read()
    
    new_content = content.replace("PASSED", "FAILED")
    file.seek(0)
    file.write(new_content)




# 9. Проверка артефактов (os.path):
# Используя модуль os.path, проверьте, был ли создан файл 'screenshot.png' (симуляция наличия скриншота после падения теста).
# Ваш код:
import os


file_path = 'screenshot.png'

if os.path.isfile(file_path):
    print(f"Файл '{file_path}' существует.")
else:
    print(f"Файл '{file_path}' не найден.")



# 10. Очистка после тестов (Cleanup):
# Удалите файл 'temp_data.csv', если он существует.
# Ваш код:
import os


file_path = 'temp_data.csv'
if os.path.isfile(file_path):
    os.remove(file_path)
    print(f"Файл '{file_path}' был успешно удален.")
else:
    print(f"Файл '{file_path}' не найден, ничего не нужно удалять.")
