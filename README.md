# AQA Python

Учебный проект по автоматизации тестирования на Python.

## Структура проекта

```text
tests/
└── test_sample.py

hello.py
requirements.txt
.gitignore
README.md
```

## Запуск проекта с нуля

### 1. Создать виртуальное окружение

```bash
python3 -m venv .venv
```

### 2. Активировать виртуальное окружение

На macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Установить зависимости

```bash
python -m pip install -r requirements.txt
```

### 4. Запустить тесты

```bash
python -m pytest
```

Если всё настроено правильно, тесты должны завершиться успешно.