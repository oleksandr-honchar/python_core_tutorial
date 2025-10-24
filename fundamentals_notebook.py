# %% [markdown]
# # 🐍 Python Fundamentals: Input/Output та Functions
# 
# ## 📚 Зміст модуля
# 
# ### Частина 1: Input та Output
# 1. Функція `print()` - виведення даних
# 2. Функція `input()` - отримання даних від користувача
# 3. Перетворення типів даних
# 4. F-strings та форматування
# 5. **Робота з файлами замість input** (практичний підхід)
# 6. Використання бібліотек для читання даних
# 
# ### Частина 2: Functions
# 1. Основи функцій
# 2. Параметри та повернення значень
# 3. Області видимості змінних
# 4. Лямбда-функції
# 5. Вбудовані функції Python
# 6. Практичні приклади з використанням бібліотек
# 
# ---

# %% [markdown]
# # 📤 Частина 1: Input та Output в Python
# 
# ## 1.1 Функція `print()` - Основи виведення даних
# 
# Функція `print()` - це основний спосіб виведення інформації у Python. Вона має багато корисних параметрів, які роблять її дуже гнучкою.
# 
# ### Основні параметри:
# - `sep` - роздільник між елементами (за замовчуванням - пробіл)
# - `end` - символ в кінці виведення (за замовчуванням - `\n`)
# - `file` - куди виводити (за замовчуванням - консоль)
# - `flush` - чи очищувати буфер негайно

# %%
# Базове використання print()
print("=" * 80)
print("1. ОСНОВИ print()")
print("=" * 80)

# Простий текст
print("Привіт, світ!")

# Виведення різних типів даних
print(42)
print(3.14159)
print(True)
print([1, 2, 3, 4, 5])

# Виведення декількох значень
print("Ім'я:", "Іван", "Вік:", 25, "Місто:", "Київ")

# %% [markdown]
# ### Параметри `sep` та `end`
# 
# Параметр `sep` дозволяє вказати, як розділяти елементи при виведенні.  
# Параметр `end` визначає, що виводити в кінці (за замовчуванням - новий рядок).

# %%
# Використання sep (separator)
print("Python", "Java", "JavaScript", "C++", sep=" | ")
print("2025", "01", "15", sep="-")
print(1, 2, 3, 4, 5, sep=" -> ")

# Використання end
print("Цей рядок ", end="")
print("продовжується на тій самій лінії!")

# Комбінація sep та end
print("Перший", "Другий", "Третій", sep=", ", end=" -> ")
print("Четвертий")

# %% [markdown]
# ### Виведення у файл
# 
# `print()` може виводити не тільки в консоль, але й у файли. Це корисно для логування або збереження результатів.

# %%
# Виведення у файл
with open('/home/claude/output_example.txt', 'w', encoding='utf-8') as f:
    print("Це виведення у файл", file=f)
    print("Можна виводити багато рядків", file=f)
    print("Дата:", "2025-01-15", file=f)

# Читаємо, що записали
with open('/home/claude/output_example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("\nВміст файлу:")
    print(content)

# %% [markdown]
# ## 1.2 Форматування виведення
# 
# Python надає кілька способів форматування рядків. Розглянемо їх від старих до сучасних.

# %%
name = "Олександр"
age = 28
height = 1.82
balance = 1234.567

print("\n" + "=" * 80)
print("СПОСОБИ ФОРМАТУВАННЯ РЯДКІВ")
print("=" * 80)

# 1. Старий спосіб - конкатенація (❌ НЕ РЕКОМЕНДУЄТЬСЯ)
print("Старий спосіб: Мене звати " + name + ", мені " + str(age) + " років")

# 2. Метод format() (✓ гарний, але застарілий)
print("Метод format(): Мене звати {}, мені {} років".format(name, age))
print("З індексами: {0} має {1} років. {0} живе в Україні".format(name, age))
print("З іменами: {n} має {a} років".format(n=name, a=age))

# 3. F-strings (✅ РЕКОМЕНДУЄТЬСЯ - Python 3.6+)
print(f"F-string: Мене звати {name}, мені {age} років")

# %% [markdown]
# ### F-strings - Потужність та гнучкість
# 
# F-strings (formatted string literals) - це найсучасніший та найзручніший спосіб форматування в Python. Вони підтримують:
# - Вирази всередині дужок
# - Виклики функцій
# - Форматування чисел
# - Вирівнювання тексту

# %%
# Вирази у f-strings
print(f"\nВирази у f-strings:")
print(f"Через 5 років мені буде {age + 5} років")
print(f"Подвоєний вік: {age * 2}")
print(f"Зріст у см: {height * 100}")

# Форматування чисел
print(f"\nФорматування чисел:")
print(f"Баланс: {balance:.2f} грн")  # 2 знаки після коми
print(f"Баланс: {balance:,.2f} грн")  # З розділювачем тисяч
print(f"Баланс: {balance:>15.2f} грн")  # Вирівнювання праворуч (15 символів)
print(f"Баланс: {balance:<15.2f} грн")  # Вирівнювання ліворуч
print(f"Баланс: {balance:^15.2f} грн")  # По центру

# Відсотки та наукова нотація
accuracy = 0.95847
print(f"\nТочність: {accuracy:.2%}")  # Як відсоток
big_number = 1234567890
print(f"Велике число: {big_number:e}")  # Наукова нотація

# %% [markdown]
# ### Математичне форматування
# 
# Для математичних констант та обчислень краще використовувати вбудовану бібліотеку `math`.

# %%
import math

print("\n" + "=" * 80)
print("ВИКОРИСТАННЯ МОДУЛЯ math")
print("=" * 80)

# ❌ НЕ РОБІТЬ ТАК:
pi_bad = 3.14
print(f"Погана практика: π ≈ {pi_bad}")

# ✅ РОБІТЬ ТАК:
print(f"Гарна практика: π = {math.pi}")
print(f"Число e: {math.e}")
print(f"τ (тау): {math.tau}")

# Форматування математичних констант
print(f"\nπ з різною точністю:")
print(f"2 знаки: {math.pi:.2f}")
print(f"5 знаків: {math.pi:.5f}")
print(f"10 знаків: {math.pi:.10f}")

# Математичні операції
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"\nКоло з радіусом {radius}:")
print(f"Площа: {area:.2f}")
print(f"Довжина кола: {circumference:.2f}")

# %% [markdown]
# ## 1.3 Функція `input()` - Отримання даних від користувача
# 
# `input()` зупиняє виконання програми та чекає введення від користувача. Завжди повертає **рядок (string)**!
# 
# ### ⚠️ Важливо розуміти:
# - У реальних проектах `input()` використовується рідко
# - Дані зазвичай беруться з файлів, баз даних, API або веб-форм
# - `input()` корисний для навчання та простих скриптів

# %%
# Базове використання input() (закоментовано для автоматичного запуску)
# name = input("Введіть ваше ім'я: ")
# print(f"Привіт, {name}!")

# Для демонстрації використаємо змінну
name = "Андрій"  # замість input()
print(f"Привіт, {name}!")

# Важливо! input() завжди повертає рядок
# age_str = input("Скільки вам років? ")
age_str = "25"  # замість input()
print(f"Ви ввели: '{age_str}' (тип: {type(age_str).__name__})")

# %% [markdown]
# ## 1.4 Перетворення типів даних (Type Casting)
# 
# Оскільки `input()` повертає рядок, часто потрібно конвертувати дані в інші типи:
# - `int()` - ціле число
# - `float()` - дробове число
# - `str()` - рядок
# - `bool()` - логічне значення
# - `list()`, `tuple()`, `set()` - колекції

# %%
print("\n" + "=" * 80)
print("ПЕРЕТВОРЕННЯ ТИПІВ ДАНИХ")
print("=" * 80)

# Перетворення рядків у числа
age_str = "28"
age_int = int(age_str)
print(f"Рядок '{age_str}' -> Число {age_int}")
print(f"Типи: {type(age_str).__name__} -> {type(age_int).__name__}")

price_str = "19.99"
price_float = float(price_str)
print(f"\nРядок '{price_str}' -> Float {price_float}")
print(f"Типи: {type(price_str).__name__} -> {type(price_float).__name__}")

# Перетворення чисел у рядки
number = 42
text = str(number)
print(f"\nЧисло {number} -> Рядок '{text}'")
print(f"Типи: {type(number).__name__} -> {type(text).__name__}")

# Перетворення у bool
print("\nПеретворення у bool:")
print(f"bool(0) = {bool(0)}")  # False
print(f"bool(1) = {bool(1)}")  # True
print(f"bool(-5) = {bool(-5)}")  # True
print(f"bool('') = {bool('')}")  # False (порожній рядок)
print(f"bool('text') = {bool('text')}")  # True

# %% [markdown]
# ### Обробка помилок при перетворенні
# 
# При перетворенні типів можуть виникати помилки. Важливо їх обробляти!

# %%
# Приклад безпечного перетворення
def safe_int_conversion(value):
    """Безпечне перетворення у int з обробкою помилок"""
    try:
        return int(value)
    except ValueError:
        print(f"❌ Помилка: '{value}' не можна перетворити у число!")
        return None

# Тести
print("\n" + "=" * 80)
print("БЕЗПЕЧНЕ ПЕРЕТВОРЕННЯ ТИПІВ")
print("=" * 80)

result1 = safe_int_conversion("123")
print(f"'123' -> {result1}")

result2 = safe_int_conversion("abc")
print(f"'abc' -> {result2}")

result3 = safe_int_conversion("12.5")
print(f"'12.5' -> {result3}")

# %% [markdown]
# ## 1.5 📁 Робота з файлами замість `input()` - Практичний підхід
# 
# ### Чому файли краще за input()?
# 
# 1. **Автоматизація**: Не потрібно вручну вводити дані кожен раз
# 2. **Великі обсяги даних**: Легко працювати з тисячами записів
# 3. **Повторюваність**: Можна багато разів запускати з тими самими даними
# 4. **Реальність**: У реальних проектах дані завжди з файлів/БД/API
# 5. **Тестування**: Легше тестувати код
# 
# ### Формати файлів:
# - **TXT** - простий текст
# - **CSV** - табличні дані (Comma Separated Values)
# - **JSON** - структуровані дані
# - **Excel** (.xlsx) - таблиці з форматуванням

# %%
# Створимо приклади файлів для роботи
print("\n" + "=" * 80)
print("СТВОРЕННЯ ТЕСТОВИХ ФАЙЛІВ")
print("=" * 80)

# 1. Створення простого текстового файлу
with open('/home/claude/user_data.txt', 'w', encoding='utf-8') as f:
    f.write("Олександр\n")
    f.write("28\n")
    f.write("Київ\n")
    f.write("1.82\n")

print("✅ Створено user_data.txt")

# 2. Створення CSV файлу
import csv

with open('/home/claude/employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Ім\'я', 'Вік', 'Місто', 'Зарплата'])
    writer.writerow(['Олександр', 28, 'Київ', 50000])
    writer.writerow(['Марія', 25, 'Львів', 48000])
    writer.writerow(['Іван', 32, 'Одеса', 55000])
    writer.writerow(['Світлана', 29, 'Київ', 52000])

print("✅ Створено employees.csv")

# 3. Створення JSON файлу
import json

data = {
    "users": [
        {"name": "Олександр", "age": 28, "city": "Київ", "skills": ["Python", "SQL"]},
        {"name": "Марія", "age": 25, "city": "Львів", "skills": ["JavaScript", "React"]},
        {"name": "Іван", "age": 32, "city": "Одеса", "skills": ["Java", "Spring"]}
    ]
}

with open('/home/claude/users.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Створено users.json")

# %% [markdown]
# ### Читання простого текстового файлу

# %%
print("\n" + "=" * 80)
print("ЧИТАННЯ ТЕКСТОВОГО ФАЙЛУ")
print("=" * 80)

# Спосіб 1: Читання всього файлу
with open('/home/claude/user_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("Весь вміст файлу:")
    print(content)

# Спосіб 2: Читання по рядках
with open('/home/claude/user_data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    name = lines[0].strip()
    age = int(lines[1].strip())
    city = lines[2].strip()
    height = float(lines[3].strip())
    
    print(f"\nРозпарсені дані:")
    print(f"Ім'я: {name}")
    print(f"Вік: {age}")
    print(f"Місто: {city}")
    print(f"Зріст: {height} м")

# %% [markdown]
# ### Читання CSV файлу
# 
# CSV (Comma-Separated Values) - це один з найпопулярніших форматів для табличних даних. Python має вбудований модуль `csv`, але ще краще використовувати `pandas`.

# %%
print("\n" + "=" * 80)
print("ЧИТАННЯ CSV - Базовий спосіб")
print("=" * 80)

# Спосіб 1: Вбудований модуль csv
import csv

with open('/home/claude/employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print("Співробітники:")
    for row in reader:
        print(f"  {row['Ім\'я']}, {row['Вік']} років, "
              f"{row['Місто']}, {row['Зарплата']} грн")

# %% [markdown]
# ### Читання CSV за допомогою pandas
# 
# **pandas** - це потужна бібліотека для роботи з даними. Вона робить роботу з CSV набагато простішою!
# 
# Переваги pandas:
# - Автоматичне визначення типів даних
# - Зручні методи для аналізу
# - Легка фільтрація та сортування
# - Інтеграція з іншими бібліотеками

# %%
# Спосіб 2: pandas (РЕКОМЕНДУЄТЬСЯ для табличних даних)
import pandas as pd

print("\n" + "=" * 80)
print("ЧИТАННЯ CSV - pandas")
print("=" * 80)

# Читаємо CSV
df = pd.read_csv('/home/claude/employees.csv')

print("Повна таблиця:")
print(df)

print("\n" + "-" * 40)
print("Базова статистика:")
print(df.describe())

print("\n" + "-" * 40)
print("Середня зарплата по містах:")
print(df.groupby('Місто')['Зарплата'].mean())

# Фільтрація
print("\n" + "-" * 40)
print("Співробітники з Києва:")
kyiv_employees = df[df['Місто'] == 'Київ']
print(kyiv_employees)

# %% [markdown]
# ### Читання JSON файлу
# 
# JSON (JavaScript Object Notation) - популярний формат для структурованих даних, особливо в веб-розробці та API.

# %%
print("\n" + "=" * 80)
print("ЧИТАННЯ JSON")
print("=" * 80)

with open('/home/claude/users.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Користувачі:")
for user in data['users']:
    print(f"\n👤 {user['name']}:")
    print(f"   Вік: {user['age']}")
    print(f"   Місто: {user['city']}")
    print(f"   Навички: {', '.join(user['skills'])}")

# %% [markdown]
# ### Приклад: Калькулятор з читанням даних з файлу
# 
# Порівняємо два підходи: input() vs файли

# %%
print("\n" + "=" * 80)
print("КАЛЬКУЛЯТОР: input() VS файли")
print("=" * 80)

# ❌ Старий підхід з input() (незручний для багатократного використання)
def calculator_with_input():
    """Калькулятор з input - потрібно вводити кожен раз вручну"""
    # num1 = float(input("Введіть перше число: "))
    # num2 = float(input("Введіть друге число: "))
    # operation = input("Операція (+, -, *, /): ")
    
    # Для демонстрації:
    num1, num2, operation = 10, 5, "+"
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = None
    
    print(f"{num1} {operation} {num2} = {result}")

# ✅ Сучасний підхід з файлами (автоматизація)
def calculator_with_file(filename):
    """Калькулятор з файлом - можна обробити багато операцій автоматично"""
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 3:
                continue
            
            num1 = float(parts[0])
            operation = parts[1]
            num2 = float(parts[2])
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
            
            print(f"{num1} {operation} {num2} = {result}")

# Створюємо файл з операціями
with open('/home/claude/calculations.txt', 'w') as f:
    f.write("10 + 5\n")
    f.write("20 - 8\n")
    f.write("7 * 6\n")
    f.write("100 / 4\n")
    f.write("15 * 3\n")

print("\nПідхід з файлом (можна обробити багато операцій):")
calculator_with_file('/home/claude/calculations.txt')

# %% [markdown]
# ## 1.6 📊 Використання спеціалізованих бібліотек
# 
# Python має безліч бібліотек, які вже реалізують типові задачі. Не варто "винаходити велосипед"!

# %%
print("\n" + "=" * 80)
print("СПЕЦІАЛІЗОВАНІ БІБЛІОТЕКИ")
print("=" * 80)

# 1. datetime - робота з датою та часом
from datetime import datetime, timedelta

print("\n📅 datetime - Робота з датою і часом:")
now = datetime.now()
print(f"Зараз: {now}")
print(f"Форматовано: {now.strftime('%d.%m.%Y %H:%M:%S')}")
print(f"Через тиждень: {now + timedelta(days=7)}")

# 2. random - випадкові числа
import random

print("\n🎲 random - Випадкові числа:")
print(f"Випадкове число (0-100): {random.randint(0, 100)}")
print(f"Випадкове float (0-1): {random.random():.4f}")
print(f"Вибір зі списку: {random.choice(['Python', 'Java', 'C++', 'JavaScript'])}")

# 3. statistics - статистика
import statistics

data = [23, 45, 67, 23, 89, 12, 45, 67, 89, 45]
print("\n📊 statistics - Статистика:")
print(f"Дані: {data}")
print(f"Середнє: {statistics.mean(data):.2f}")
print(f"Медіана: {statistics.median(data)}")
print(f"Мода: {statistics.mode(data)}")
print(f"Стандартне відхилення: {statistics.stdev(data):.2f}")

# 4. pathlib - робота зі шляхами
from pathlib import Path

print("\n📁 pathlib - Робота зі шляхами:")
current_file = Path('/home/claude/output_example.txt')
print(f"Існує: {current_file.exists()}")
print(f"Розширення: {current_file.suffix}")
print(f"Ім'я файлу: {current_file.name}")
print(f"Директорія: {current_file.parent}")

# %% [markdown]
# ---
# 
# # 🔧 Частина 2: Functions (Функції)
# 
# ## 2.1 Що таке функція?
# 
# **Функція** - це іменований блок коду, який виконує конкретну задачу. Функції - основа модульного програмування.
# 
# ### Навіщо потрібні функції?
# 
# 1. **DRY принцип** (Don't Repeat Yourself) - не повторюйте код
# 2. **Читабельність** - код легше читати та розуміти
# 3. **Тестування** - легше тестувати окремі функції
# 4. **Повторне використання** - одну функцію можна використовувати багато разів
# 5. **Абстракція** - ховаємо складність реалізації
# 
# ### Синтаксис:
# ```python
# def function_name(parameters):
#     """Docstring - опис функції"""
#     # код функції
#     return result
# ```

# %%
print("\n" + "=" * 80)
print("ОСНОВИ ФУНКЦІЙ")
print("=" * 80)

# Найпростіша функція
def say_hello():
    """Виводить привітання"""
    print("Привіт!")

say_hello()
say_hello()  # Можна викликати багато разів

# Функція з параметром
def greet(name):
    """
    Вітає користувача за ім'ям
    
    Args:
        name (str): Ім'я користувача
    """
    print(f"Привіт, {name}!")

greet("Олександр")
greet("Марія")

# Функція з кількома параметрами
def greet_with_time(name, time_of_day):
    """Вітає з урахуванням часу доби"""
    print(f"Доброго {time_of_day}, {name}!")

greet_with_time("Іван", "ранку")
greet_with_time("Світлана", "вечора")

# %% [markdown]
# ## 2.2 Повернення значень (return)
# 
# Функції можуть не тільки виконувати дії, але й **повертати результат** за допомогою `return`.

# %%
print("\n" + "=" * 80)
print("ПОВЕРНЕННЯ ЗНАЧЕНЬ")
print("=" * 80)

# Функція, що повертає значення
def add(a, b):
    """Додає два числа"""
    return a + b

# Використання результату
result = add(5, 3)
print(f"5 + 3 = {result}")

# Можна використовувати у виразах
total = add(10, 20) + add(5, 15)
print(f"(10+20) + (5+15) = {total}")

# Функція з множинними return
def absolute_value(x):
    """Повертає абсолютне значення числа"""
    if x >= 0:
        return x
    else:
        return -x

print(f"|5| = {absolute_value(5)}")
print(f"|-7| = {absolute_value(-7)}")

# %% [markdown]
# ### Повернення декількох значень
# 
# Python дозволяє повертати кілька значень одночасно (насправді це кортеж).

# %%
def divide_with_remainder(a, b):
    """
    Ділить числа з остачею
    
    Args:
        a: Ділене
        b: Дільник
    
    Returns:
        tuple: (частка, остача)
    """
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Розпакування результату
q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} (остача {r})")

# Або як кортеж
result = divide_with_remainder(23, 7)
print(f"23 ÷ 7 = {result}")

# %% [markdown]
# ## 2.3 Параметри за замовчуванням
# 
# Параметри можуть мати значення за замовчуванням. Це робить функції більш гнучкими.

# %%
print("\n" + "=" * 80)
print("ПАРАМЕТРИ ЗА ЗАМОВЧУВАННЯМ")
print("=" * 80)

def power(base, exponent=2):
    """
    Піднесення до степеня
    
    Args:
        base: Основа
        exponent: Показник степеня (за замовчуванням 2)
    """
    return base ** exponent

# Використання значення за замовчуванням
print(f"5^2 = {power(5)}")

# Вказуємо свій показник
print(f"5^3 = {power(5, 3)}")
print(f"2^10 = {power(2, 10)}")

# Функція для привітання
def greet_person(name, greeting="Привіт", punctuation="!"):
    """Гнучке привітання"""
    return f"{greeting}, {name}{punctuation}"

print(greet_person("Андрій"))
print(greet_person("Марія", "Вітаю"))
print(greet_person("Іван", "Доброго дня", "."))

# %% [markdown]
# ## 2.4 Іменовані аргументи (keyword arguments)
# 
# При виклику функції можна вказувати назви параметрів. Це покращує читабельність!

# %%
print("\n" + "=" * 80)
print("ІМЕНОВАНІ АРГУМЕНТИ")
print("=" * 80)

def create_profile(name, age, city, occupation):
    """Створює профіль користувача"""
    return {
        'name': name,
        'age': age,
        'city': city,
        'occupation': occupation
    }

# Позиційні аргументи (не дуже читабельно)
profile1 = create_profile("Олександр", 28, "Київ", "Developer")
print(profile1)

# Іменовані аргументи (набагато зрозуміліше!)
profile2 = create_profile(
    name="Марія",
    age=25,
    city="Львів",
    occupation="Designer"
)
print(profile2)

# Можна змінювати порядок
profile3 = create_profile(
    age=30,
    name="Іван",
    occupation="Manager",
    city="Одеса"
)
print(profile3)

# %% [markdown]
# ## 2.5 *args та **kwargs - Змінна кількість аргументів
# 
# - `*args` - дозволяє передавати довільну кількість позиційних аргументів
# - `**kwargs` - дозволяє передавати довільну кількість іменованих аргументів

# %%
print("\n" + "=" * 80)
print("*args ТА **kwargs")
print("=" * 80)

# *args - змінна кількість позиційних аргументів
def sum_all(*args):
    """Сума всіх переданих чисел"""
    return sum(args)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20) = {sum_all(10, 20)}")

# **kwargs - змінна кількість іменованих аргументів
def print_info(**kwargs):
    """Виводить інформацію у вигляді ключ: значення"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nІнформація про користувача:")
print_info(name="Олександр", age=28, city="Київ", job="Developer")

print("\nІнформація про продукт:")
print_info(title="Ноутбук", price=25000, brand="Dell", color="Сірий")

# Комбінація всього
def create_user(name, *hobbies, **details):
    """Створює користувача з хобі та додатковою інфою"""
    print(f"\nКористувач: {name}")
    print(f"Хобі: {', '.join(hobbies)}")
    print("Додаткова інформація:")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_user(
    "Марія",
    "Читання", "Подорожі", "Фотографія",
    age=25,
    city="Львів",
    occupation="Дизайнер"
)

# %% [markdown]
# ## 2.6 Лямбда-функції (анонімні функції)
# 
# **Лямбда-функції** - це маленькі анонімні функції, які можна створити в один рядок.
# 
# Синтаксис: `lambda arguments: expression`
# 
# Використовуйте лямбда-функції для:
# - Простих операцій
# - Коротких callback-функцій
# - Сортування та фільтрації

# %%
print("\n" + "=" * 80)
print("ЛЯМБДА-ФУНКЦІЇ")
print("=" * 80)

# Звичайна функція
def square(x):
    return x ** 2

# Те саме через лямбду
square_lambda = lambda x: x ** 2

print(f"square(5) = {square(5)}")
print(f"square_lambda(5) = {square_lambda(5)}")

# Лямбда з кількома параметрами
add = lambda a, b: a + b
multiply = lambda a, b: a * b

print(f"\n10 + 5 = {add(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")

# Використання з вбудованими функціями
numbers = [1, 2, 3, 4, 5]

# map() - застосувати функцію до кожного елемента
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nКвадрати: {numbers} -> {squared}")

# filter() - відфільтрувати елементи
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Парні: {evens}")

# sorted() з лямбдою для сортування
students = [
    {'name': 'Олександр', 'grade': 85},
    {'name': 'Марія', 'grade': 92},
    {'name': 'Іван', 'grade': 78},
    {'name': 'Світлана', 'grade': 95}
]

sorted_students = sorted(students, key=lambda s: s['grade'], reverse=True)
print("\nСтуденти за оцінкою (від вищої до нижчої):")
for student in sorted_students:
    print(f"  {student['name']}: {student['grade']}")

# %% [markdown]
# ## 2.7 Області видимості (Scope)
# 
# Python має різні області видимості змінних:
# 
# 1. **Local** - всередині функції
# 2. **Enclosing** - у зовнішній функції (для вкладених функцій)
# 3. **Global** - на рівні модуля
# 4. **Built-in** - вбудовані імена Python

# %%
print("\n" + "=" * 80)
print("ОБЛАСТІ ВИДИМОСТІ")
print("=" * 80)

# Глобальна змінна
global_var = "Я глобальна"

def outer_function():
    # Змінна зовнішньої функції (enclosing)
    enclosing_var = "Я enclosing"
    
    def inner_function():
        # Локальна змінна
        local_var = "Я локальна"
        
        print(f"  Локальна: {local_var}")
        print(f"  Enclosing: {enclosing_var}")
        print(f"  Глобальна: {global_var}")
    
    inner_function()
    print(f"  У зовнішній функції: {enclosing_var}")
    # print(local_var)  # ❌ Помилка!

outer_function()
print(f"Глобальна змінна: {global_var}")

# Модифікація глобальної змінної
counter = 0

def increment_bad():
    """❌ Не спрацює - створить локальну змінну"""
    counter = counter + 1  # UnboundLocalError!

def increment_good():
    """✅ Правильно - використовуємо global"""
    global counter
    counter += 1

print(f"\nЛічильник до: {counter}")
increment_good()
print(f"Лічильник після: {counter}")
increment_good()
print(f"Лічильник після: {counter}")

# %% [markdown]
# ## 2.8 Вбудовані функції Python
# 
# Python має багато вбудованих функцій. Використовуйте їх замість власних реалізацій!

# %%
print("\n" + "=" * 80)
print("ВБУДОВАНІ ФУНКЦІЇ PYTHON")
print("=" * 80)

numbers = [23, 45, 12, 67, 89, 34, 56]

# Математичні функції
print("Математичні функції:")
print(f"  sum: {sum(numbers)}")
print(f"  min: {min(numbers)}")
print(f"  max: {max(numbers)}")
print(f"  abs(-10): {abs(-10)}")
print(f"  pow(2, 10): {pow(2, 10)}")
print(f"  round(3.14159, 2): {round(3.14159, 2)}")

# Робота з колекціями
print("\nРобота з колекціями:")
print(f"  len: {len(numbers)}")
print(f"  sorted: {sorted(numbers)}")
print(f"  reversed: {list(reversed(numbers))}")

# Робота з типами
print("\nПеревірка типів:")
print(f"  isinstance(5, int): {isinstance(5, int)}")
print(f"  isinstance('text', str): {isinstance('text', str)}")
print(f"  type(3.14): {type(3.14)}")

# Робота з рядками та ітераторами
print("\nРобота з ітераторами:")
print(f"  all([True, True, True]): {all([True, True, True])}")
print(f"  all([True, False, True]): {all([True, False, True])}")
print(f"  any([False, False, True]): {any([False, False, True])}")

# enumerate - нумерація елементів
print("\nenumerate:")
fruits = ['яблуко', 'банан', 'апельсин']
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# zip - об'єднання списків
print("\nzip:")
names = ['Олександр', 'Марія', 'Іван']
ages = [28, 25, 32]
for name, age in zip(names, ages):
    print(f"  {name}: {age} років")

# %% [markdown]
# ## 2.9 Декоратори - Розширення функціональності
# 
# **Декоратори** дозволяють модифікувати поведінку функцій без зміни їх коду.
# 
# Типові використання:
# - Логування
# - Вимірювання часу виконання
# - Перевірка прав доступу
# - Кешування результатів

# %%
import time
import functools

print("\n" + "=" * 80)
print("ДЕКОРАТОРИ")
print("=" * 80)

# Простий декоратор для логування
def log_function_call(func):
    """Декоратор для логування викликів функції"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📞 Виклик функції: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Функція {func.__name__} завершена")
        return result
    return wrapper

@log_function_call
def calculate_sum(a, b):
    """Додає два числа"""
    return a + b

result = calculate_sum(10, 20)
print(f"Результат: {result}\n")

# Декоратор для вимірювання часу
def measure_time(func):
    """Вимірює час виконання функції"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} виконувалась {end - start:.6f} секунд")
        return result
    return wrapper

@measure_time
def slow_function():
    """Повільна функція для демонстрації"""
    time.sleep(0.1)  # Імітація роботи
    return sum(range(100000))

result = slow_function()
print(f"Результат: {result}\n")

# Комбінація декораторів
@log_function_call
@measure_time
def complex_calculation(n):
    """Складне обчислення"""
    return sum(i ** 2 for i in range(n))

result = complex_calculation(10000)
print(f"Результат: {result}")

# %% [markdown]
# ## 2.10 Документування функцій (Docstrings)
# 
# **Docstring** - це рядок документації на початку функції. Він описує що робить функція, які приймає параметри та що повертає.
# 
# ### Формати docstring:
# - **Google Style** (рекомендується)
# - NumPy Style
# - reStructuredText

# %%
print("\n" + "=" * 80)
print("ДОКУМЕНТУВАННЯ ФУНКЦІЙ")
print("=" * 80)

def calculate_bmi(weight, height):
    """
    Обчислює індекс маси тіла (BMI).
    
    BMI = вага (кг) / (зріст (м))²
    
    Args:
        weight (float): Вага в кілограмах
        height (float): Зріст в метрах
    
    Returns:
        float: Індекс маси тіла
    
    Raises:
        ValueError: Якщо вага або зріст <= 0
    
    Examples:
        >>> calculate_bmi(70, 1.75)
        22.86
        
        >>> calculate_bmi(85, 1.80)
        26.23
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Вага та зріст мають бути додатними числами")
    
    return weight / (height ** 2)

# Використання
bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}")

# Перегляд документації
print("\nДокументація функції:")
print(calculate_bmi.__doc__)

# Або через help()
# help(calculate_bmi)

# %% [markdown]
# ## 2.11 Практичні приклади з використанням бібліотек
# 
# Розглянемо реальні приклади, де функції працюють з даними з файлів та бібліотеками.

# %%
print("\n" + "=" * 80)
print("ПРАКТИЧНІ ПРИКЛАДИ")
print("=" * 80)

# Приклад 1: Аналіз даних з CSV
def analyze_employees(filename):
    """
    Аналізує дані про співробітників з CSV файлу
    
    Args:
        filename (str): Шлях до CSV файлу
    
    Returns:
        dict: Статистика по співробітникам
    """
    df = pd.read_csv(filename)
    
    stats = {
        'total_employees': len(df),
        'average_age': df['Вік'].mean(),
        'average_salary': df['Зарплата'].mean(),
        'cities': df['Місто'].unique().tolist(),
        'salary_by_city': df.groupby('Місто')['Зарплата'].mean().to_dict()
    }
    
    return stats

# Використання
stats = analyze_employees('/home/claude/employees.csv')
print("\n📊 Статистика співробітників:")
print(f"Всього співробітників: {stats['total_employees']}")
print(f"Середній вік: {stats['average_age']:.1f} років")
print(f"Середня зарплата: {stats['average_salary']:.2f} грн")
print(f"Міста: {', '.join(stats['cities'])}")
print("Середня зарплата по містах:")
for city, salary in stats['salary_by_city'].items():
    print(f"  {city}: {salary:.2f} грн")

# %% [markdown]
# ### Приклад 2: Робота з датами

# %%
from datetime import datetime, timedelta

def calculate_age(birth_date_str):
    """
    Обчислює вік на основі дати народження
    
    Args:
        birth_date_str (str): Дата народження у форматі 'YYYY-MM-DD'
    
    Returns:
        int: Вік у роках
    """
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - birth_date.year
    
    # Коригуємо, якщо день народження ще не настав цього року
    if today.month < birth_date.month or \
       (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age

def days_until_birthday(birth_date_str):
    """Обчислює кількість днів до наступного дня народження"""
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    today = datetime.now()
    
    # Наступний день народження
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    days = (next_birthday - today).days
    return days

# Тестування
birth_date = "1995-06-15"
print(f"\nДата народження: {birth_date}")
print(f"Вік: {calculate_age(birth_date)} років")
print(f"Днів до дня народження: {days_until_birthday(birth_date)}")

# %% [markdown]
# ### Приклад 3: Обробка текстових даних

# %%
import re
from collections import Counter

def analyze_text_file(filename):
    """
    Аналізує текстовий файл
    
    Args:
        filename (str): Шлях до текстового файлу
    
    Returns:
        dict: Статистика по тексту
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Видаляємо пунктуацію і переводимо в нижній регістр
    words = re.findall(r'\b[а-яіїєґa-z]+\b', text.lower())
    
    stats = {
        'total_characters': len(text),
        'total_words': len(words),
        'unique_words': len(set(words)),
        'average_word_length': sum(len(word) for word in words) / len(words) if words else 0,
        'most_common_words': Counter(words).most_common(5)
    }
    
    return stats

# Створюємо тестовий файл
test_text = """
Python це потужна мова програмування.
Python підтримує різні парадигми програмування.
Програмування на Python це цікаво та корисно.
Python використовується для веб-розробки, аналізу даних та машинного навчання.
"""

with open('/home/claude/test_text.txt', 'w', encoding='utf-8') as f:
    f.write(test_text)

# Аналіз
text_stats = analyze_text_file('/home/claude/test_text.txt')
print("\n📝 Аналіз тексту:")
print(f"Всього символів: {text_stats['total_characters']}")
print(f"Всього слів: {text_stats['total_words']}")
print(f"Унікальних слів: {text_stats['unique_words']}")
print(f"Середня довжина слова: {text_stats['average_word_length']:.2f}")
print("\nНайпопулярніші слова:")
for word, count in text_stats['most_common_words']:
    print(f"  {word}: {count} раз(ів)")

# %% [markdown]
# ### Приклад 4: Математичні обчислення з numpy

# %%
import numpy as np

def calculate_statistics(data):
    """
    Обчислює статистику для масиву даних
    
    Args:
        data (list or np.array): Дані для аналізу
    
    Returns:
        dict: Статистичні показники
    """
    arr = np.array(data)
    
    return {
        'mean': np.mean(arr),
        'median': np.median(arr),
        'std': np.std(arr),
        'min': np.min(arr),
        'max': np.max(arr),
        'percentile_25': np.percentile(arr, 25),
        'percentile_75': np.percentile(arr, 75)
    }

def normalize_data(data):
    """Нормалізує дані до діапазону [0, 1]"""
    arr = np.array(data)
    min_val = np.min(arr)
    max_val = np.max(arr)
    return (arr - min_val) / (max_val - min_val)

# Тестування
data = [23, 45, 12, 67, 89, 34, 56, 78, 23, 45]

print("\n🔢 Статистичний аналіз:")
stats = calculate_statistics(data)
for key, value in stats.items():
    print(f"  {key}: {value:.2f}")

print("\nОригінальні дані:", data)
print("Нормалізовані:", normalize_data(data).round(3).tolist())

# %% [markdown]
# ## 2.12 Рекурсивні функції
# 
# **Рекурсія** - це коли функція викликає саму себе. Потужний інструмент для розв'язання певних задач.
# 
# ### Коли використовувати рекурсію:
# - Робота з деревовидними структурами
# - Математичні послідовності (факторіал, Фібоначчі)
# - Обхід файлової системи
# - Алгоритми "розділяй і володарюй"

# %%
print("\n" + "=" * 80)
print("РЕКУРСИВНІ ФУНКЦІЇ")
print("=" * 80)

# Приклад 1: Факторіал
def factorial(n):
    """
    Обчислює факторіал числа рекурсивно
    
    Args:
        n (int): Невід'ємне ціле число
    
    Returns:
        int: n! = n * (n-1) * (n-2) * ... * 1
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Факторіали:")
for i in range(6):
    print(f"  {i}! = {factorial(i)}")

# Приклад 2: Числа Фібоначчі
def fibonacci(n):
    """Обчислює n-те число Фібоначчі"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nЧисла Фібоначчі:")
fib_numbers = [fibonacci(i) for i in range(10)]
print(f"  Перші 10: {fib_numbers}")

# Оптимізована версія з мемоїзацією
@functools.lru_cache(maxsize=None)
def fibonacci_optimized(n):
    """Оптимізована версія Фібоначчі з кешуванням"""
    if n <= 1:
        return n
    return fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)

print(f"  50-те число Фібоначчі: {fibonacci_optimized(50)}")

# Приклад 3: Сума цифр числа
def sum_of_digits(n):
    """Рекурсивно обчислює суму цифр числа"""
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

print("\nСума цифр:")
numbers_to_test = [123, 456, 7890]
for num in numbers_to_test:
    print(f"  Сума цифр {num} = {sum_of_digits(num)}")

# %% [markdown]
# ## 2.13 Функції вищого порядку
# 
# **Функції вищого порядку** - це функції, які:
# - Приймають інші функції як аргументи
# - Повертають функції як результат
# 
# Приклади вбудованих функцій вищого порядку: `map()`, `filter()`, `reduce()`, `sorted()`

# %%
from functools import reduce

print("\n" + "=" * 80)
print("ФУНКЦІЇ ВИЩОГО ПОРЯДКУ")
print("=" * 80)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - застосувати функцію до кожного елемента
print("map() - квадрати чисел:")
squares = list(map(lambda x: x ** 2, numbers))
print(f"  {numbers}")
print(f"  {squares}")

# filter() - відфільтрувати елементи
print("\nfilter() - тільки парні:")
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  {evens}")

# reduce() - згорнути список до одного значення
print("\nreduce() - добуток всіх чисел:")
product = reduce(lambda x, y: x * y, numbers)
print(f"  {product}")

# Власна функція вищого порядку
def apply_twice(func, value):
    """Застосовує функцію двічі"""
    return func(func(value))

print("\napply_twice():")
print(f"  (5 + 1) + 1 = {apply_twice(lambda x: x + 1, 5)}")
print(f"  (2 * 2) * 2 = {apply_twice(lambda x: x * 2, 2)}")

# Функція, що повертає функцію
def make_multiplier(n):
    """Створює функцію-множник"""
    return lambda x: x * n

multiply_by_5 = make_multiplier(5)
multiply_by_10 = make_multiplier(10)

print("\nФункція, що повертає функцію:")
print(f"  7 * 5 = {multiply_by_5(7)}")
print(f"  7 * 10 = {multiply_by_10(7)}")

# %% [markdown]
# ## 2.14 Type Hints - Анотації типів
# 
# **Type hints** (підказки типів) - це спосіб вказати очікувані типи параметрів та результатів функцій. Вони покращують читабельність та допомагають виявляти помилки.
# 
# ### Переваги:
# - Краща читабельність коду
# - Підтримка IDE (автодоповнення, перевірка типів)
# - Документація коду
# - Статичний аналіз (mypy, pyright)

# %%
from typing import List, Dict, Tuple, Optional, Union

print("\n" + "=" * 80)
print("TYPE HINTS")
print("=" * 80)

def greet_user(name: str, age: int) -> str:
    """
    Вітає користувача
    
    Args:
        name: Ім'я користувача
        age: Вік користувача
    
    Returns:
        Привітальне повідомлення
    """
    return f"Привіт, {name}! Тобі {age} років."

def calculate_average(numbers: List[float]) -> float:
    """Обчислює середнє значення списку чисел"""
    return sum(numbers) / len(numbers) if numbers else 0.0

def find_user(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    """
    Шукає користувача за ID
    
    Returns:
        Словник з даними користувача або None
    """
    users = {
        1: {"name": "Олександр", "age": 28},
        2: {"name": "Марія", "age": 25}
    }
    return users.get(user_id)

def process_data(data: Union[List, Tuple]) -> int:
    """Обробляє дані у вигляді списку або кортежу"""
    return len(data)

# Використання
print(greet_user("Іван", 30))
print(f"Середнє: {calculate_average([1.5, 2.7, 3.9, 4.2]):.2f}")
print(f"Користувач: {find_user(1)}")
print(f"Користувач: {find_user(999)}")
print(f"Довжина: {process_data([1, 2, 3, 4, 5])}")

# %% [markdown]
# # 📚 Підсумок та Best Practices
# 
# ## Input/Output
# 
# ### ✅ Робіть так:
# - Використовуйте f-strings для форматування
# - Читайте дані з файлів замість `input()` для автоматизації
# - Використовуйте спеціалізовані бібліотеки (pandas, json) замість власних рішень
# - Обробляйте помилки при перетворенні типів
# - Використовуйте контекстний менеджер `with` для роботи з файлами
# 
# ### ❌ Не робіть так:
# - Не використовуйте конкатенацію рядків для форматування
# - Не забувайте про encoding='utf-8' при роботі з українським текстом
# - Не вводьте константи вручну (π = 3.14), використовуйте `math.pi`
# - Не забувайте закривати файли (або використовуйте `with`)
# 
# ## Functions
# 
# ### ✅ Робіть так:
# - Пишіть короткі функції з однією відповідальністю
# - Використовуйте docstrings для документування
# - Використовуйте type hints для ясності
# - Використовуйте параметри за замовчуванням для гнучкості
# - Використовуйте вбудовані функції замість власних реалізацій
# - Використовуйте декоратори для повторюваної логіки
# 
# ### ❌ Не робіть так:
# - Не створюйте функції-монстри з сотнями рядків
# - Не використовуйте глобальні змінні без необхідності
# - Не використовуйте мутабельні значення за замовчуванням (list, dict)
# - Не пишіть функції без документації
# 
# ---

# %% [markdown]
# # 🎯 Практичні завдання
# 
# ## Завдання 1: Аналізатор логів
# Створіть функцію, яка читає лог-файл та виводить статистику по різних типах повідомлень (INFO, WARNING, ERROR).
# 
# ## Завдання 2: Калькулятор зарплат
# Напишіть програму, яка читає CSV з працівниками (ім'я, години, ставка) та розраховує зарплату з урахуванням податків.
# 
# ## Завдання 3: Конвертер одиниць виміру
# Створіть набір функцій для конвертації різних одиниць (температура, довжина, вага, тощо).
# 
# ## Завдання 4: Обробник JSON конфігів
# Напишіть функції для читання, валідації та оновлення JSON конфігураційних файлів.
# 
# ## Завдання 5: Генератор звітів
# Створіть функцію, яка бере дані з CSV та генерує HTML звіт з таблицею та графіком.

# %% [markdown]
# # 🔗 Корисні посилання
# 
# ## Документація:
# - [Python Documentation](https://docs.python.org/3/)
# - [Python Tutorial](https://docs.python.org/3/tutorial/)
# - [PEP 8 - Style Guide](https://pep8.org/)
# 
# ## Бібліотеки:
# - [pandas Documentation](https://pandas.pydata.org/docs/)
# - [numpy Documentation](https://numpy.org/doc/)
# - [matplotlib Documentation](https://matplotlib.org/stable/contents.html)
# 
# ## Навчання:
# - [Real Python](https://realpython.com/)
# - [Python.org Tutorial](https://docs.python.org/3/tutorial/)
# - [W3Schools Python](https://www.w3schools.com/python/)
# 
# ---
# 
# ## 🎓 Завершення модуля
# 
# Ви вивчили:
# - ✅ Основи input/output в Python
# - ✅ Форматування рядків (f-strings)
# - ✅ Роботу з файлами (TXT, CSV, JSON)
# - ✅ Використання бібліотек (pandas, numpy, math)
# - ✅ Створення та використання функцій
# - ✅ Параметри, return, області видимості
# - ✅ Лямбда-функції та функції вищого порядку
# - ✅ Декоратори та type hints
# - ✅ Best practices для Python
# 
# **Наступні кроки:**
# 1. Практикуйте написання функцій
# 2. Працюйте з реальними даними
# 3. Вивчайте додаткові бібліотеки
# 4. Читайте чужий код для покращення своїх навичок
# 
# Удачі у навчанні! 🚀

# %%
print("\n" + "=" * 80)
print("✨ МОДУЛЬ ЗАВЕРШЕНО! ✨")
print("=" * 80)
print("\nДякуємо за увагу! Практикуйтесь та пишіть чистий код! 🐍")
