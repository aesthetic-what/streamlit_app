# Установка

Для начала нужно импортировать репозиторий себе на пк

```git clone https://github.com/aesthetic-what/streamlit_app.git```

# Запуск

После можно запустить через докер или вручную установить все зависимости

## Docker

Если у вас есть докер на пк, то можно сразу запустить проект
для этого нужно ввести команду

```docker compose up --build -d```

## мануальная установка

Если докера нет, то установим ручками
Для этого нужно ввести ряд команд

```pip install -r requirements.txt```

```streamlit run ./frontend/main.py```

```uvicorn backend.main:app --reload```