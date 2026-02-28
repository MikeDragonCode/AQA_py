# ПАМЯТКА: Исключения
# try:
#     # опасный код (например, поиск элемента или запрос к базе)
# except NoSuchElementException:
#     # что делать если не нашли
# except Exception as e:
#     # ловим любую ошибку и сохраняем описание в e
#
# raise AssertionError("Msg") - уронить тест с сообщением

# Домашнее задание: Исключения (AQA Focus - Обработка падений)

# 1. Безопасное деление (валидация данных):
# Напишите функцию `safe_divide(a, b)`, которая обрабатывает ZeroDivisionError.
# Она должна возвращать 0, если b равно 0.
# Ваш код:
def safe_divide(a, b):
    
    try:
        print(int(a/b))
    except ZeroDivisionError:
        print("На 0 нельзя делить")


safe_divide(10,0)

# 2. Обработка некорректного ввода:
# Запросите у пользователя `timeout`. Попробуйте преобразовать его в `int`.
# Если возникнет `ValueError` (ввели текст вместо числа) – установите timeout = 5 (по умолчанию).
# Ваш код:
def timeout(timeout):

    try:
        print(int(timeout))
    except ValueError:
        timeout = 5
        print(int(timeout))

timeout('timeout')

# 3. Несколько типов ошибок:
# Дан словарь `results = {'test_1': 'PASSED'}`.
# Попробуйте достать статус 'test_2' И разделить его результат на 0.
# Напишите отдельные блоки except для KeyError и ZeroDivisionError.
# Ваш код:
results = {'test_1': 'PASSED'}

try:
    print(results['test_2'])
except KeyError:
    print("Такого элемента в списке не найдено")

except ZeroDivisionError:
    print(results['test_2'] / 0)
    print("На ноль делить нельзя")



# 4. Гарантированное закрытие (Finally):
# В блоке `try`: напечатайте "Opening Browser".
# В блоке `except`: напечатайте "Error happened".
# В блоке `finally`: напечатайте "Closing Browser" (это должно выполниться всегда!).
# Ваш код:
try:
    print("Opening Browser")
except Exception as e:
    print("Error happened")
finally:
    print("Closing Browser")



# 5. Обработка таймаута (Simulated):
# Напишите код, который генерирует (raise) `TimeoutError`, если `is_element_visible` равно False.
is_element_visible = False

try:
    if not is_element_visible:
        raise TimeoutError("Element is not visible, operation timed out.")
except TimeoutError as e:
    print(f"Caught an exception: {e}")


# 6. Получение текста ошибки:
# Попробуйте прочитать несуществующий файл.
# Сохраните ошибку в переменную `e` и распечатайте: "Log error: {e}".
# Ваш код:
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except Exception as e:
  
    print(f"Log error: {e}")

# 7. Валидация возраста пользователя (Raise):
# Напишите функцию `validate_age(age)`. Если age < 18, выбросьте `ValueError` с сообщением "Too young for this site".
# Ваш код:

def validate_age(age):
    if age < 18:
        raise ValueError("Too young for this site")
    return True  

try:
    validate_age(16) 
except ValueError as e:
    print(f"Error: {e}") 


# 8. Кастомное исключение (QA Exception):
# Создайте свой класс `TestFailedError`, наследуемый от `Exception`.
# Используйте его для прерывания теста, если условие не выполнено.
# Ваш код:
class TestFailedError(Exception):
  
    pass

def run_test(condition):
    """Запускает тест и выбрасывает TestFailedError, если условие не выполнено."""
    if not condition:
        raise TestFailedError("Тест не пройден: условие не выполнено.")
    return "Тест пройден!"

try:
    result = run_test(False)  
    print(result)
except TestFailedError as e:
    print(f"Ошибка: {e}")  


# 9. Проброс ошибки (Reraise):
# Поймайте любую ошибку, напечатайте "Sending log to Jira..." и выбросьте ошибку СНОВА,
# чтобы тест в итоге пометился как упавший.
# Ваш код:
class TestFailedError(Exception):
 
    pass

def run_test(condition):
    
    if not condition:
        return "Тест пройден!"

try:
    result = run_test(False) 
    print(result)
except TestFailedError as e:
    print("Sending log to Jira...")  
    raise  # Пробрасываем ошибку снова, чтобы тест пометился как упавший
except Exception as e:
    print("Unexpected error occurred:", e)
    print("Sending log to Jira...")
    raise

# 10. Ассерты (Утверждения):
# Используйте ключевое слово `assert`, чтобы проверить, что 2 + 2 == 4.
# Напишите еще один ассерт, который падает и содержит ваше сообщение об ошибке.
# Ваш код:


some_condition = True


assert 2 + 2 == 4, "Ошибка: 2 + 2 не равно 4!"


assert some_condition, "Это сообщение об ошибке: some_condition должно быть True!"
