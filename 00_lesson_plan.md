# Модуль 2: Контроль потоку та функції
# Детальний план заняття

## 📋 Загальна інформація

**Тривалість:** 2.5 - 3 години  
**Формат:** Теорія + Практика + Live Coding  
**Цільова аудиторія:** Початківці в Python  

---

## 🎯 Цілі заняття

Після заняття студенти зможуть:

✅ Створювати та використовувати Git репозиторії  
✅ Працювати з VSCode для розробки на Python  
✅ Створювати функції з різними параметрами  
✅ Використовувати методи рядків  
✅ Налагоджувати код через debugger  
✅ Писати чистий та читабельний код  

---

## 📚 Структура заняття

### Частина 1: Інструменти (40-45 хв)

#### 1.1 Git/GitHub (20-25 хв)

**Теорія (5 хв):**
- Що таке система контролю версій?
- Навіщо потрібен Git?
- GitHub vs Git

**Демонстрація (15-20 хв):**

```bash
# Live демонстрація всього workflow

# 1. Створення репозиторію на GitHub
- Показати інтерфейс GitHub
- Створити новий репозиторій
- Пояснити опції (Public/Private, README, .gitignore)

# 2. Клонування
cd ~/Documents
git clone https://github.com/username/python-course-module2.git
cd python-course-module2

# 3. Створення файлу
touch hello.py
# Написати простий код
echo 'print("Hello from Git!")' > hello.py

# 4. Git workflow
git status              # Показати статус
git add hello.py        # Додати файл
git status              # Показати зміни
git commit -m "Додано hello.py"
git log                 # Показати історію
git push origin main    # Відправити на GitHub

# 5. Перевірка на GitHub
- Оновити сторінку та показати файл
```

**Практика студентів (буде вдома):**
- Створити свій репозиторій
- Склонувати його
- Додати перший файл
- Зробити commit та push

---

#### 1.2 VSCode (15-20 хв)

**Демонстрація (10-15 хв):**

1. **Відкриття проєкту:**
   ```bash
   code ~/Documents/python-course-module2
   ```

2. **Огляд інтерфейсу:**
   - Explorer (файли)
   - Редактор
   - Термінал
   - Extensions

3. **Встановлення розширень:**
   - Python (від Microsoft)
   - Pylance
   - Показати як шукати та встановлювати

4. **Базове налаштування:**
   - Font Size
   - Auto Save
   - Theme (опціонально)

5. **Демонстрація роботи:**
   ```python
   # Показати IntelliSense
   print()  # Підказка параметрів
   
   text = "Hello"
   text.  # Показати автодоповнення методів
   ```

6. **Вбудований термінал:**
   ```bash
   # Показати як відкрити (Ctrl + `)
   python hello.py
   ```

**Гарячі клавіші для показу:**
- `Ctrl+P` - швидкий пошук файлу
- `Ctrl+/` - коментар
- `F5` - запуск debugger

---

### Частина 2: Основи Python (60-80 хв)

#### 2.1 Input/Output (15 хв)

**Live Coding:**

```python
# Файл: demo_input_output.py

# 1. Базовий print
print("=" * 40)
print("Привіт, курс Python!")
print("=" * 40)

# 2. Print з параметрами
print("Ім'я:", "Олександр", "Вік:", 25)
print("Ім'я:", "Олександр", "Вік:", 25, sep=" | ")
print("Перший рядок", end=" ")
print("Той самий рядок!")

# 3. Input
name = input("Як вас звати? ")
print(f"Привіт, {name}!")

# 4. Типи даних та конвертація
age_str = input("Скільки вам років? ")
print(f"Тип: {type(age_str)}")  # <class 'str'>

age = int(age_str)
print(f"Через 5 років вам буде {age + 5}")

# 5. f-strings
print(f"Мене звати {name}, мені {age} років")

# 6. Практичний приклад
width = float(input("Ширина прямокутника: "))
height = float(input("Висота прямокутника: "))
area = width * height
print(f"Площа: {area:.2f}")
```

**Ключові моменти:**
- input() завжди повертає string
- f-strings для форматування (сучасний спосіб)
- Конвертація типів: int(), float(), str()

---

#### 2.2 Функції (25-30 хв)

**Live Coding:**

```python
# Файл: demo_functions.py

# 1. Проста функція
def say_hello():
    """Виводить привітання"""
    print("Привіт!")
    print("Як справи?")

say_hello()
say_hello()  # Можна викликати багато разів

# 2. Функція з параметрами
def greet(name):
    """Вітає користувача за ім'ям"""
    print(f"Привіт, {name}!")

greet("Олександр")
greet("Марія")

# 3. Функція з return
def add_numbers(a, b):
    """Додає два числа"""
    result = a + b
    return result

sum1 = add_numbers(5, 3)
print(f"5 + 3 = {sum1}")

# Можна використовувати у виразах
total = add_numbers(10, 20) + add_numbers(5, 5)
print(f"Загальна сума: {total}")

# 4. Параметри за замовчуванням
def greet_with_time(name, time="ранку"):
    """Вітає з часом доби"""
    print(f"Доброго {time}, {name}!")

greet_with_time("Іван")  # Використає "ранку"
greet_with_time("Петро", "вечора")

# 5. Повернення декількох значень
def divide_with_remainder(a, b):
    """Ділить з остачею"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} (остача {r})")

# 6. Docstring
def calculate_area(width, height):
    """
    Обчислює площу прямокутника.
    
    Args:
        width: Ширина
        height: Висота
    
    Returns:
        float: Площа
    """
    return width * height

# Показати документацію
print(calculate_area.__doc__)
```

**Інтерактивна частина:**
- Попросити студентів передбачити результат
- Задати питання: "Що виведе ця функція?"
- Разом написати функцію для площі трикутника

**Завдання для студентів (5 хв):**
```python
# Самостійно напишіть функцію
def multiply(a, b):
    """Множить два числа"""
    # Ваш код тут
    pass

# Тест
print(multiply(4, 5))  # Має вивести 20
```

---

#### 2.3 Робота з рядками (20-25 хв)

**Live Coding:**

```python
# Файл: demo_strings.py

# 1. Базові операції
text = "Python"
print(f"Перший символ: {text[0]}")
print(f"Останній: {text[-1]}")
print(f"Довжина: {len(text)}")

# 2. Зрізи
word = "Programming"
print(word[0:4])    # Prog
print(word[:4])     # Prog
print(word[4:])     # ramming
print(word[::-1])   # gnimmargorP (реверс)

# 3. Методи - регістр
text = "hello World"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.capitalize()) # Hello world
print(text.title())      # Hello World

# 4. Методи - пошук
sentence = "Python is awesome"
print(sentence.find("is"))        # 7
print(sentence.count("o"))        # 2
print(sentence.startswith("Python"))  # True

# 5. Методи - перевірка
print("123".isdigit())   # True
print("abc".isalpha())   # True

# 6. Видалення пробілів
text = "   Python   "
print(f"'{text.strip()}'")   # 'Python'

# 7. Заміна
text = "Я вивчаю Java"
new_text = text.replace("Java", "Python")
print(new_text)

# 8. Розділення та об'єднання
sentence = "Python is easy"
words = sentence.split()  # ['Python', 'is', 'easy']
print(words)

joined = " ".join(words)
print(joined)

# 9. Практичний приклад: пошук літери
def find_letter(text, letter):
    """Шукає літеру у тексті"""
    # Спосіб 1: простий
    if letter in text:
        return True
    
    # Спосіб 2: через цикл
    for char in text:
        if char.lower() == letter.lower():
            return True
    return False

result = find_letter("Hello", "e")
print(f"Літера знайдена: {result}")

# 10. Пошук всіх позицій
def find_all_positions(text, letter):
    """Знаходить всі позиції літери"""
    positions = []
    for i in range(len(text)):
        if text[i].lower() == letter.lower():
            positions.append(i)
    return positions

positions = find_all_positions("Hello World", "o")
print(f"Позиції 'o': {positions}")
```

**Показати документацію:**
```python
# У VSCode показати:
text = "example"
text.  # IntelliSense покаже всі методи

# Або у браузері:
# https://docs.python.org/3/library/stdtypes.html#string-methods
```

**Інтерактив:**
- "Як зробити реверс рядка?"
- "Як перевірити чи всі символи - цифри?"
- Разом написати функцію для підрахунку голосних

---

#### 2.4 Debugging (15-20 хв)

**Демонстрація VSCode Debugger:**

```python
# Файл: demo_debug.py

def calculate_sum(numbers):
    """Рахує суму чисел"""
    total = 0  # BREAKPOINT ТУТ (червона крапка)
    
    for number in numbers:
        total = total + number
        print(f"Поточна сума: {total}")
    
    return total

result = calculate_sum([5, 10, 15, 20])
print(f"Результат: {result}")
```

**Покрокова демонстрація:**

1. **Додати breakpoint:**
   - Клікнути ліворуч від номера рядка
   - Показати червону крапку

2. **Запустити debugger:**
   - Натиснути F5
   - Вибрати "Python File"

3. **Показати панель Debug:**
   ```
   ▶️ Continue (F5)
   🔄 Step Over (F10)
   ⬇️ Step Into (F11)
   ⏹️ Stop
   ```

4. **Показати Variables:**
   - Ліва панель
   - Locals: total, number, numbers
   - Як змінюються значення

5. **Step Over (F10):**
   - Клікнути F10
   - Показати як змінюється total
   - Пройти всі ітерації циклу

6. **Watch:**
   - Додати вираз: `total * 2`
   - Показати як відстежується

**Другий приклад - з помилкою:**

```python
def find_average_bug():
    """Функція з багом"""
    numbers = [10, 20, 30]
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        # count += 1  # БАГ: забули!!!
    
    average = total / count  # Ділення на 0!
    return average

# find_average_bug()
```

**Демонстрація пошуку помилки:**
1. Breakpoint на першому рядку
2. Step Over через цикл
3. Дивитись на count (залишається 0!)
4. Знайти проблему
5. Виправити код

---

### Частина 3: Практика (30-40 хв)

#### 3.1 Спільне coding (15-20 хв)

**Завдання 1: Площа трикутника**
```python
def triangle_area(base, height):
    """
    Обчислює площу трикутника
    Формула: (base * height) / 2
    """
    # Пишемо разом зі студентами
    area = (base * height) / 2
    return area

# Тестуємо
print(triangle_area(10, 5))  # 25.0
print(triangle_area(7, 4))   # 14.0
```

**Завдання 2: Перевірка паліндрому**
```python
def is_palindrome(word):
    """
    Перевіряє чи слово паліндром
    """
    # Разом зі студентами:
    # 1. Привести до нижнього регістру
    # 2. Порівняти з реверсом
    
    word_lower = word.lower()
    reversed_word = word_lower[::-1]
    return word_lower == reversed_word

# Тести
print(is_palindrome("шалаш"))  # True
print(is_palindrome("python")) # False
```

---

#### 3.2 Самостійна робота (15-20 хв)

**Завдання для студентів:**

1. **Легкий рівень:**
   ```python
   # Напишіть функцію, яка перевіряє чи число парне
   def is_even(number):
       # Ваш код
       pass
   ```

2. **Середній рівень:**
   ```python
   # Напишіть функцію для конвертації температури
   def celsius_to_fahrenheit(celsius):
       # Формула: (C × 9/5) + 32
       pass
   ```

3. **Складніший рівень:**
   ```python
   # Напишіть функцію для підрахунку голосних
   def count_vowels(text):
       # Голосні: a, e, i, o, u
       pass
   ```

**Формат роботи:**
- Студенти пишуть код самостійно (10 хв)
- Викладач допомагає індивідуально
- Розбір рішень разом (5-10 хв)

---

### Частина 4: Підсумки та домашнє завдання (10-15 хв)

#### 4.1 Рекапітуляція

**Що ми пройшли:**
```
✅ Git/GitHub:
   - Створення репозиторію
   - clone, add, commit, push
   - Базовий workflow

✅ VSCode:
   - Налаштування
   - Розширення
   - Debugger

✅ Python основи:
   - input() та print()
   - Функції (параметри, return, docstring)
   - Методи рядків
   - Debugging

✅ Практичні навички:
   - Написання чистого коду
   - Пошук помилок
   - Робота з документацією
```

#### 4.2 Домашнє завдання

**Інструкція:**

1. **Створіть репозиторій:**
   - Назва: `python-homework-module2`
   - Додайте README.md з описом

2. **Виконайте завдання:**
   
   Файл: `homework.py`
   
   ```python
   # Завдання 1: Пошук літери (5 балів)
   def find_letter_positions(text, letter):
       """
       Знаходить всі позиції літери у тексті
       
       Returns:
           list: Список індексів
       """
       pass  # Ваш код
   
   
   # Завдання 2: Калькулятор (5 балів)
   def calculate(a, b, operation):
       """
       Виконує арифметичну операцію
       
       Args:
           operation: '+', '-', '*', '/'
       
       Returns:
           float: Результат
       """
       pass  # Ваш код
   
   
   # Завдання 3: Площа фігур (5 балів)
   def triangle_area(base, height):
       """Площа трикутника"""
       pass
   
   def circle_area(radius):
       """Площа кола (π ≈ 3.14159)"""
       pass
   
   
   # Завдання 4: Робота з текстом (5 балів)
   def count_words(text):
       """Рахує кількість слів"""
       pass
   
   def reverse_words(text):
       """Реверс порядку слів"""
       pass
   
   
   # БОНУС: Паліндром (2 бали)
   def is_palindrome(text):
       """Перевіряє паліндром"""
       pass
   ```

3. **Тестування:**
   
   Файл: `test_homework.py`
   
   ```python
   from homework import *
   
   # Тести для перевірки
   print("=" * 50)
   print("ТЕСТУВАННЯ")
   print("=" * 50)
   
   # Тест 1
   print(find_letter_positions("Hello", "l"))  # [2, 3]
   
   # Тест 2
   print(calculate(10, 5, '+'))  # 15.0
   print(calculate(10, 5, '*'))  # 50.0
   
   # Тест 3
   print(triangle_area(10, 5))   # 25.0
   print(circle_area(5))         # 78.54
   
   # Тест 4
   print(count_words("Hello World"))  # 2
   print(reverse_words("Hello World"))  # "World Hello"
   
   # Бонус
   print(is_palindrome("radar"))  # True
   ```

4. **Здача:**
   ```bash
   git add .
   git commit -m "Completed homework module 2"
   git push origin main
   ```
   
   Надіслати посилання на репозиторій

**Критерії оцінювання:**
- Завдання 1-4: по 5 балів (20 балів)
- Бонус: 2 бали
- Чистий код і коментарі: 3 бали
- **Максимум: 25 балів**

---

## 📖 Додаткові матеріали

### Для студентів:

**Документація:**
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Git Book](https://git-scm.com/book/uk/v2)

**Практика:**
- [Python Tutor](http://pythontutor.com) - візуалізація виконання коду
- [Repl.it](https://replit.com) - онлайн IDE
- [DataLemur](https://datalemur.com) - задачі для практики (пізніше для SQL)

**Відео:**
- Corey Schafer - Git Tutorial
- Real Python - VSCode Setup

---

## 💡 Поради для викладача

### Перед заняттям:
- [ ] Протестувати всі приклади коду
- [ ] Перевірити що Git встановлений
- [ ] Підготувати GitHub демо-репозиторій
- [ ] Встановити VSCode + розширення
- [ ] Підготувати запасні приклади

### Під час заняття:
- [ ] Заохочувати питання
- [ ] Робити паузи для перевірки розуміння
- [ ] Використовувати інтерактив
- [ ] Показувати різні підходи до розв'язання
- [ ] Використовувати debugger для пояснення

### Типові запитання студентів:

**Q: Чому input() повертає string?**  
A: Для універсальності. Користувач може ввести що завгодно. Ми конвертуємо типи за потреби.

**Q: Коли використовувати функції?**  
A: Коли код повторюється, або коли хочемо розбити складну задачу на частини.

**Q: Навіщо docstring?**  
A: Документація коду. Допомагає іншим (та вам через місяць) зрозуміти що робить функція.

**Q: Як запам'ятати всі методи рядків?**  
A: Не треба! Використовуйте автодоповнення в VSCode та документацію.

---

## ⏱️ Тайм-менеджмент

```
00:00 - 00:10  Вступ та організаційні моменти
00:10 - 00:30  Git/GitHub демонстрація
00:30 - 00:50  VSCode налаштування
00:50 - 01:00  ПЕРЕРВА
01:00 - 01:15  Input/Output
01:15 - 01:45  Функції
01:45 - 02:10  Рядки
02:10 - 02:25  Debugging
02:25 - 02:35  ПЕРЕРВА
02:35 - 02:55  Спільне coding
02:55 - 03:15  Самостійна робота
03:15 - 03:30  Підсумки та ДЗ
```

---

## ✅ Чеклист успішного заняття

- [ ] Всі студенти встановили VSCode
- [ ] Всі створили GitHub репозиторій
- [ ] Всі зробили перший commit і push
- [ ] Всі написали мінімум одну функцію
- [ ] Всі спробували debugger
- [ ] Всі отримали домашнє завдання
- [ ] Відповіли на всі питання

---

**Успіхів на занятті! 🚀**
