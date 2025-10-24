# Git/GitHub: Інструкція для здачі домашнього завдання

## 🎯 Мета
Навчитися працювати з системою контролю версій Git та платформою GitHub для здачі домашніх завдань.

---

## 1️⃣ Створення репозиторію на GitHub

### Крок 1: Реєстрація/Вхід
- Перейдіть на [github.com](https://github.com)
- Зареєструйтеся або увійдіть в свій акаунт

### Крок 2: Створення нового репозиторію
1. Натисніть на `+` у верхньому правому куті
2. Виберіть `New repository`
3. Заповніть форму:
   - **Repository name**: `python-course-module2` (або інша назва)
   - **Description**: "Домашні завдання модуль 2"
   - **Public/Private**: оберіть Public (для навчання)
   - ✅ Поставте галочку "Add a README file"
   - Оберіть `.gitignore`: Python
4. Натисніть `Create repository`

**🎉 Вітаємо! Ваш репозиторій створено!**

---

## 2️⃣ Клонування репозиторію на ПК

### Перевірка встановлення Git
Відкрийте термінал/командний рядок і виконайте:
```bash
git --version
```

Якщо Git не встановлений, завантажте з [git-scm.com](https://git-scm.com)

### Клонування
1. На сторінці репозиторію натисніть зелену кнопку `Code`
2. Скопіюйте HTTPS URL (наприклад: `https://github.com/username/python-course-module2.git`)
3. У терміналі перейдіть до папки, де хочете зберегти проєкт:
   ```bash
   cd ~/Documents  # або інша папка
   ```
4. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/username/python-course-module2.git
   ```
5. Перейдіть у папку проєкту:
   ```bash
   cd python-course-module2
   ```

---

## 3️⃣ Робота з файлами та коммітами

### Створення файлу з домашнім завданням
```bash
# Створіть файл
touch homework_01.py

# Або використайте VSCode для створення файлу
```

### Базовий workflow Git

#### 1. Перегляд статусу
```bash
git status
```
Показує які файли змінені, додані чи видалені.

#### 2. Додавання файлів до staging area
```bash
# Додати конкретний файл
git add homework_01.py

# Додати всі змінені файли
git add .

# Додати всі файли з розширенням .py
git add *.py
```

#### 3. Створення коммміту
```bash
git commit -m "Додано рішення завдання 1"
```

**💡 Поради для commit messages:**
- Пишіть зрозумілі повідомлення
- Починайте з дієслова: "Додано", "Виправлено", "Оновлено"
- Приклади:
  - ✅ "Додано функцію для пошуку літери"
  - ✅ "Виправлено помилку в обчисленні площі"
  - ❌ "asdf"
  - ❌ "фіналка"

#### 4. Відправка на GitHub (push)
```bash
git push origin main
```

**Якщо це перший push і просить authentication:**
- Використайте Personal Access Token замість пароля
- [Як створити токен](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

---

## 4️⃣ Типовий workflow для домашнього завдання

```bash
# 1. Переконайтесь, що ви в папці проєкту
cd python-course-module2

# 2. Оновіть локальну копію (якщо були зміни на GitHub)
git pull origin main

# 3. Створіть/відредагуйте файл з завданням
code homework_01.py  # відкриється VSCode

# 4. Перевірте статус
git status

# 5. Додайте файли
git add homework_01.py

# 6. Створіть комміт
git commit -m "Виконано завдання 1: функція пошуку літери"

# 7. Відправте на GitHub
git push origin main
```

---

## 5️⃣ Отримання архіву з GitHub

### Метод 1: Через веб-інтерфейс
1. Перейдіть на сторінку репозиторію
2. Натисніть зелену кнопку `Code`
3. Виберіть `Download ZIP`

### Метод 2: Через командний рядок (створення архіву)
```bash
# Створити zip архів
git archive -o homework_module2.zip HEAD

# Або tar.gz
git archive -o homework_module2.tar.gz HEAD
```

---

## 🆘 Корисні команди Git

```bash
# Подивитися історію коммітів
git log

# Коротка історія
git log --oneline

# Подивитися зміни у файлах
git diff

# Скасувати зміни у файлі (до git add)
git checkout -- filename.py

# Видалити файл з staging area (після git add)
git reset HEAD filename.py

# Подивитися інформацію про remote репозиторій
git remote -v
```

---

## 🎓 Чеклист для здачі ДЗ

- [ ] Репозиторій створено на GitHub
- [ ] Репозиторій склоновано на локальний комп'ютер
- [ ] Код написано та перевірено
- [ ] Файли додано через `git add`
- [ ] Зроблено комміт з осмисленим повідомленням
- [ ] Код відправлено на GitHub через `git push`
- [ ] Перевірено на GitHub, що файли там є

---

## 📚 Додаткові ресурси

- [Git Book (офіційна документація)](https://git-scm.com/book/uk/v2)
- [GitHub Guides](https://guides.github.com/)
- [Візуалізація Git команд](https://git-school.github.io/visualizing-git/)
- [Learn Git Branching (інтерактивний курс)](https://learngitbranching.js.org/)

---

## 🐛 Типові проблеми та рішення

### Помилка: "Permission denied"
- Переконайтеся, що ви використовуєте правильний URL
- Використайте HTTPS замість SSH (якщо не налаштували SSH ключі)
- Використайте Personal Access Token замість пароля

### Помилка: "fatal: not a git repository"
- Ви не в папці з git репозиторієм
- Виконайте `cd` до правильної папки

### Конфлікти при push
- Спочатку зробіть `git pull`
- Вирішіть конфлікти у файлах
- Зробіть комміт та push знову

---

**Успіхів у навчанні! 🚀**
