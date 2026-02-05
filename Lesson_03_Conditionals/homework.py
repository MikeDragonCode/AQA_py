# ПАМЯТКА: Условные конструкции
# if condition:
# elif condition:
# else:
#
# Логические операторы: and, or, not
# is - проверка идентичности (None, True, False)
# in - проверка вхождения

# Домашнее задание: Условные конструкции (AQA Focus)

# 1. Проверка статус-кода (API тестирование):
# Дана переменная status_code = 404.
# Если код 200 - выведите "OK".
# Если 201 - выведите "Created".
# Если 404 - выведите "Not Found".
# Если 500 - выведите "Internal Server Error".
# Иначе - "Unknown Status".
status_code = 404
# Ваш код:

# 2. Проверка прав доступа:
# Даны переменные: role = "admin" (или "guest") и is_authorized = True.
# Если пользователь авторизован И роль "admin" - выведите "Access Granted".
# Иначе - "Access Denied".
role = "admin"
is_authorized = True
# Ваш код:

# 3. Тернарный оператор для отчета:
# Есть переменная test_passed = False.
# Создайте переменную message, которая равна "Test Success", если test_passed True,
# и "Test Failure", если False. (Используйте одну строку).
test_passed = False
# Ваш код:

# 4. Валидация входных данных:
# В переменную username пришло значение None (симуляция бага API, где поле отсутствует).
# Если username is None или пустая строка "" - выведите "Error: Username required".
# Иначе - "Username is valid".
username = None
# Ваш код:

# 5. Проверка вхождений (Response Body):
# Пришел ответ от сервера: response_text = "{"error": "User not found"}".
# Если в ответе есть слово "error" или "fail" - выведите "Test Failed".
# Иначе - "Response OK".
response_text = '{"error": "User not found"}'
# Ваш код:

# 6. Вложенные проверки (Логика теста):
# Есть element_visible = True и element_enabled = True.
# Если элемент виден:
#    Если элемент активен (enabled) -> "Clicking element".
#    Иначе -> "Element visible but disabled".
# Иначе -> "Element not found".
element_visible = True
element_enabled = True
# Ваш код:

# 7. Оператор not (Инверсия):
# Есть список ошибок errors = [].
# Если список ошибок ПУСТ (not errors) - выведите "No bugs found!".
# Иначе - "Found bugs".
errors = []
# Ваш код:

# 8. Сложные условия (Бизнес-логика):
# Скидка применяется, если:
# (сумма > 1000) ИЛИ (есть промокод И сумма > 500).
# Реализуйте проверку.
amount = 800
has_promo = True
# Ваш код:

# 9. Match-case (Python 3.10+):
# Реализуйте обработку действий браузера.
# action = "click" -> выведите "Clicking..."
# action = "type" -> выведите "Typing..."
# action = "wait" -> выведите "Waiting..."
# _ -> "Unknown action"
action = "click"
# Ваш код:

# 10. Проверка типа данных (валидация JSON):
# Получено значение value = "123".
# Если это строка (str) - выведите "It's a string".
# Если число (int) - "It's a number".
# Используйте isinstance().
value = "123"
# Ваш код:
