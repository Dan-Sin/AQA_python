# AQA Python

Учебный проект по автоматизации тестирования на Python.

## Структура проекта

```text
tests/
├── api/
├── ui/
├── conftest.py
├── test_module_fixture.py
├── test_parametrize.py
└── test_second_file.py

pytest.ini
requirements.txt
.env.example
.gitignore
README.md
```

## Запуск проекта с нуля

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Dan-Sin/AQA_python
```

### 2. Перейти в папку проекта

```bash
cd PythonProject
```

### 3. Создать виртуальное окружение

```bash
python3 -m venv .venv
```

### 4. Активировать виртуальное окружение

На macOS / Linux:

```bash
source .venv/bin/activate
```

### 5. Установить зависимости

```bash
python -m pip install -r requirements.txt
```

### 6. Запустить все тесты

```bash
python -m pytest
```

### 7. Запустить только тесты с маркером math

```bash
python -m pytest -m math
```

Если всё настроено правильно, тесты должны завершиться успешно.