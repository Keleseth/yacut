# YaCut - Сервис для создания коротких ссылок

![Flask](https://img.shields.io/badge/flask-%23000000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Alembic](https://img.shields.io/badge/alembic-%230071C5.svg?style=for-the-badge&logo=alembic&logoColor=white) ![Jinja2](https://img.shields.io/badge/jinja2-%23B41717.svg?style=for-the-badge&logo=jinja&logoColor=white) ![Marshmallow](https://img.shields.io/badge/marshmallow-%2300A1E0.svg?style=for-the-badge&logo=python&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23F47216.svg?style=for-the-badge&logo=python&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Описание
YaCut — это сервис для сокращения URL, позволяющий создать короткую версию ссылки, которой легко делиться с другими. Проект реализован на Python с использованием Flask и поддерживает как API, так и веб-интерфейс.


## Установка
Клонируйте репозиторий и перейдите в папку с проектом:
```bash
git clone <repository-url>
```
```bash
cd <project-repository>
```
### Flask ожидает наличие файла .env в корневой папке проекта с 4 переменными:
- FLASK_APP= название приложения. По умолчанию yacut
- FLASK_DEBUG= дебаг мод
- DATABASE_URI= строка подключения к базе данных.
- SECRET_KEY= секретная строка на ваше усмотрение.

## Установка виртуального окружения и зависимостей
1.  Установите виртуальное окружение и активируйте его:

Если у вас Windows:
```bash
python -m venv venv
source \venv\Scripts\activate
```

или Если у вас Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Установите зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск проекта
После установки зависимостей, запустите сервер приложения:

```bash
flask run
```
По умолчанию проект будет доступен по адресу http://127.0.0.1:5000

## Примеры использования
### Веб-интерфейс
Перейдя по адресу сервиса http://127.0.0.1:5000 вы попадете на главную страницу сервиса. 
В поле длинной ссылки следует вводить оригинальную ссылку для перехода, в поле короткой ссылки
пользовательский вариант короткой ссылки. Если короткая ссылка не будет предоставлена, сервер сгенерирует
её случайным образом из 6 символов латинского алфавита и цифр от 0 до 9. Длинная и короткая ссылки будут связаны, 
при переходе по короткой ссылке, пользователь будет переадресован по оригинальной длинной ссылке.

### API-интерфейс
Проект поддерживает API для создания и получения коротких ссылок.
Полная документация доступна перейдя по адресу https://editor.swagger.io/ и вставив в редактор содержимое файла openapi.yml в корневой папке проекта.


Проект разработан Келесидисом Александром. GitHub: [Keleseth](https://github.com/Keleseth)