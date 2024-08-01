# Todos API

___

Todos API - Django-project to set your missions for today.

## Installation

___

1. Clone the repository:

```git 
clone https://github.com/islomkambarov5/Todos-rest-project
```

2. Install the dependencies:
```terminal
pip install -r requirements.txt
```

3. Apply migrations
```
python manage.py migrate
```
```
python manage.py makemigrations
```

4. Create super user(admin)
```
python manage.py createsuperuser
```

5. Run the development server:

```
python manage.py runserver
```


## Usage
___
### Endpoints
___

- **GET `/api/`**: Retrieve a list of your todos
- **POST `/api/`**: Create a new todo
- **GET `/api/{id}/`**: Retrieve a todo with this id
- **PUT `/api/{id}/`**: Update a todo with this id
- **DELETE `api/delete/{id}`**: Delete a todo with this id

### Example Requests

1. Get a list of your todos:

```http
GET /api/
```

#### Create a new todo and update a todo a todo:

After authentication, at the end of correct page you can update and create todo
