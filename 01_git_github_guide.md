# Git/GitHub: Інструкція для здачі домашнього завдання

## 🎯 Мета

Навчитися працювати з системою контролю версій Git та платформою GitHub для здачі домашніх завдань.

---

## 0️⃣ Налаштування доступу та ключів (SSH або HTTPS+PAT)

### 0.1 Оберіть спосіб доступу

* **SSH‑ключі** — зручно для щоденної роботи, без введення логіну/пароля при кожному `push`.
* **HTTPS + Personal Access Token (PAT)** — альтернатива без SSH (зручно на корпоративних ПК, де заборонено SSH).

### 0.2 Налаштуйте дані користувача Git (один раз на ПК)

```bash
git config --global user.name "Ваше Ім'я"
git config --global user.email "your_email@example.com"
# (необов'язково) більш зручний редактор для повідомлень комітів
git config --global core.editor "code --wait"
```

### 0.3 Створення SSH‑ключа

> Рекомендований тип: **ed25519** (сучасний та безпечний). Якщо система не підтримує — використайте `rsa -b 4096`.

```bash
# Створити ключ (замініть email на ваш GitHub email)
ssh-keygen -t ed25519 -C "your_email@example.com"
# Коли запитає шлях, залиште типовий (~/.ssh/id_ed25519) і задайте пароль (passphrase) за бажанням.
```

### 0.4 Запуск ssh‑agent та додавання ключа (саме тут потрібен `eval`)

**macOS / Linux:**

```bash
# Запустити агента та експортувати змінні середовища
eval "$(ssh-agent -s)"
# Додати приватний ключ у агент
ssh-add ~/.ssh/id_ed25519
```

**Windows (PowerShell):**

```powershell
# Увімкнути та запустити службу ssh-agent (один раз)
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
# Додати ключ
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

### 0.5 Додавання публічного ключа на GitHub

1. Скопіюйте публічний ключ:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   # macOS: pbcopy < ~/.ssh/id_ed25519.pub
   # Windows (Git Bash): clip < ~/.ssh/id_ed25519.pub
   ```
2. Перейдіть в GitHub → **Settings** → **SSH and GPG keys** → **New SSH key**.
3. Вставте ключ і збережіть.

### 0.6 Перевірка підключення до GitHub

```bash
ssh -T git@github.com
# Успішний результат виглядає так:
# Hi <ваш-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

> Якщо хочете діагностику, додайте `-v` для детального логу: `ssh -vT git@github.com`.

### 0.7 Використання ключа саме для GitHub (за потреби)

Створіть/відредагуйте файл `~/.ssh/config`:

```sshconfig
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```

### 0.8 Переключення remote‑URL на SSH (з HTTPS)

```bash
git remote -v  # перевірити поточні URL
# Приклад заміни для вашого репозиторію
git remote set-url origin git@github.com:username/python-course-module2.git
```

### 0.9 Альтернатива: HTTPS + Personal Access Token (PAT)

1. Створіть PAT: GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained** (або **Classic**) → дайте доступ **repo**.
2. При `git push` використовуйте **username** і **PAT** як пароль.
3. (Опціонально) збереження облікових даних:

   * macOS: `git config --global credential.helper osxkeychain`
   * Windows: `git config --global credential.helper manager`
   * Linux (простий варіант): `git config --global credential.helper store` *(зберігає у відкритому вигляді — використовуйте обережно!)*

### 0.10 Типові помилки з SSH та як виправити

* **Permission denied (publickey)**

  * Переконайтесь, що ключ додано в агент: `ssh-add -l` (має відображати ваш ключ).
  * Ключ додано в GitHub (пункт 0.5).
  * Права доступу: `chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_ed25519`.
* **Agent admitted failure to sign** — перезапустіть агент та перевстановіть ключ у агент (`eval "$(ssh-agent -s)"`, потім `ssh-add ...`).
* **Host key verification failed** — оновіть запис у `known_hosts`:

  ```bash
  ssh-keygen -R github.com
  ssh -T git@github.com
  ```

---

## 1️⃣ Створення репозиторію на GitHub

### Крок 1: Реєстрація/Вхід

* Перейдіть на [github.com](https://github.com)
* Зареєструйтеся або увійдіть в свій акаунт

### Крок 2: Створення нового репозиторію

1. Натисніть на `+` у верхньому правому куті
2. Виберіть `New repository`
3. Заповніть форму:

   * **Repository name**: `python-course-module2` (або інша назва)
   * **Description**: "Домашні завдання модуль 2"
   * **Public/Private**: оберіть Public (для навчання)
   * ✅ Поставте галочку "Add a README file"
   * Оберіть `.gitignore`: Python
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

1. На сторінці репозиторію натисніть зелену кнопку `Code`.
2. Оберіть **SSH** (якщо налаштовані ключі) **або** HTTPS.
3. Скопіюйте URL, наприклад:

   * SSH: `git@github.com:username/python-course-module2.git`
   * HTTPS: `https://github.com/username/python-course-module2.git`
4. У терміналі перейдіть до папки, де хочете зберегти проєкт:

   ```bash
   cd ~/Documents  # або інша папка
   ```
5. Клонуйте репозиторій:

   ```bash
   git clone git@github.com:username/python-course-module2.git
   # або (HTTPS)
   # git clone https://github.com/username/python-course-module2.git
   ```
6. Перейдіть у папку проєкту:

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

#### 3. Створення комміту

```bash
git commit -m "Додано рішення завдання 1"
```

**💡 Поради для commit messages:**

* Пишіть зрозумілі повідомлення
* Починайте з дієслова: "Додано", "Виправлено", "Оновлено"
* Приклади:

  * ✅ "Додано функцію для пошуку літери"
  * ✅ "Виправлено помилку в обчисленні площі"
  * ❌ "asdf"
  * ❌ "фіналка"

#### 4. Відправка на GitHub (push)

```bash
git push origin main
```

**Якщо це перший push і просить аутентифікацію:**

* При **HTTPS** — використайте **Personal Access Token** замість пароля.
* При **SSH** — запитів не буде (за умови, що ключі налаштовано й додано до ssh‑agent).

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

### Метод 1: Через веб‑інтерфейс

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

## 🎓 Чекліст для здачі ДЗ

* [ ] Налаштовано доступ (SSH‑ключі або HTTPS+PAT)
* [ ] Перевірено підключення (`ssh -T git@github.com` або перший `push` по HTTPS)
* [ ] Репозиторій створено на GitHub
* [ ] Репозиторій склоновано на локальний комп'ютер
* [ ] Код написано та перевірено
* [ ] Файли додано через `git add`
* [ ] Зроблено комміт з осмисленим повідомленням
* [ ] Код відправлено на GitHub через `git push`
* [ ] Перевірено на GitHub, що файли там є

---

## 📚 Додаткові ресурси

* [Git Book (офіційна документація)](https://git-scm.com/book/uk/v2)
* [GitHub Guides](https://guides.github.com/)
* [Візуалізація Git команд](https://git-school.github.io/visualizing-git/)
* [Learn Git Branching (інтерактивний курс)](https://learngitbranching.js.org/)

---

## 🐛 Типові проблеми та рішення

### Помилка: "Permission denied"

* Для **SSH**: додайте ключ у агент (`ssh-add`), перевірте права файлів, переконайтесь, що ключ додано в GitHub.
* Для **HTTPS**: використовуйте **PAT** замість пароля.

### Помилка: "fatal: not a git repository"

* Ви не в папці з git репозиторієм — виконайте `cd` до правильної папки.

### Конфлікти при push

* Спочатку зробіть `git pull`
* Вирішіть конфлікти у файлах
* Зробіть комміт та push знову

---

**Успіхів у навчанні! 🚀**
