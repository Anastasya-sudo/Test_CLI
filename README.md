# gh-summary

📊 **gh-summary** — это простой CLI-инструмент, который выводит краткую информацию о GitHub-проекте на основе имени пользователя и названия репозитория.

---

## Стек технологий
- python3.11

---

## 📦 Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Anastasya-sudo/Test_CLI.git
cd Test_CLI
```

---

##  Создание виртуального окружения и установка

> ⚠️ Перед установкой убедитесь, что у вас установлен Python 3.10+ и pip.


### ✅ Linux / macOS

```bash
# создать виртуальное окружение
python3 -m venv venv

# активировать его
source venv/bin/activate

# установить проект как CLI
pip install .
```

---

### ✅ Windows (PowerShell)

```powershell
# создать виртуальное окружение
python -m venv venv

# активировать его
.env\Scriptsctivate

# установить проект как CLI
pip install .
```

---

## 🚀 Запуск

После установки доступна команда `gh-summary`:

```bash
gh-summary -u <github_username> -p <repository_name>
```

Пример:

```bash
gh-summary -u Anastasya-sudo -p Test_CLI
```

Ожидаемый результат:

```
Generating summary for https://github.com/Anastasya-sudo/Test_CLI
```

---

## 🔧 Альтернативный запуск (если команда не работает)

Если по какой-то причине команда `gh-summary` не запускается, можно использовать Python напрямую:

```bash
python -m gh_summary -u Anastasya-sudo -p Test_CLI
```

---

## 📁 Структура проекта

```
Test_CLI/
├── gh_summary/
│   ├── __init__.py
│   └── __main__.py
├── setup.py
└── README.md
```

---

## Команда

---

## 🛠 Зависимости

- Python 3.10+
- requests (устанавливается автоматически через `pip install .`)

---

## Ссылки

---

## 📄 Лицензия

Этот проект доступен под лицензией MIT.
