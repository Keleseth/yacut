# YaCut - URL Shortening Service

![Flask](https://img.shields.io/badge/flask-%23000000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Alembic](https://img.shields.io/badge/alembic-%230071C5.svg?style=for-the-badge&logo=alembic&logoColor=white) ![Jinja2](https://img.shields.io/badge/jinja2-%23B41717.svg?style=for-the-badge&logo=jinja&logoColor=white) ![Marshmallow](https://img.shields.io/badge/marshmallow-%2300A1E0.svg?style=for-the-badge&logo=python&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23F47216.svg?style=for-the-badge&logo=python&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Description
YaCut is a URL shortening service that allows you to create a short version of a link, which is easy to share. The project is implemented in Python using Flask and supports both API and web interfaces.


## Installation
Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
```
```bash
cd <project-repository>
```
### Flask expects an .env file in the root directory of the project with 4 variables:
- FLASK_APP: Application name. By default, it is set to yacut.
- FLASK_DEBUG: Debug mode.
- DATABASE_URI: Database connection URI.
- SECRET_KEY: A secret string of your choice.

## Setting up a virtual environment and dependencies
1.  Create and activate a virtual environment:

If you are on Windows:
```bash
python -m venv venv
source \venv\Scripts\activate
```

or you are on Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the project
After installing the dependencies, start the application server:

```bash
flask run
```
By default, the project will be available at http://127.0.0.1:5000

## Usage Examples
### Web Interface
Navigate to the service URL at http://127.0.0.1:5000 to access the main page of the service. In the "Long link" field, you should enter the original link to be shortened, and in the "Short link" field, you can enter a custom short link of your choice. If no short link is provided, the server will generate one randomly using 6 characters from the Latin alphabet and digits from 0 to 9. The long and short links will be associated, and when you access the short link, you will be redirected to the original long link.

### API Interface
The project supports an API for creating and retrieving short links. Full documentation is available by visiting https://editor.swagger.io/ and inserting the content of the openapi.yml file located in the root folder of the project.


The project was developed by Alexander Kelesidis. GitHub: [Keleseth](https://github.com/Keleseth)