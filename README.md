# Django_Store_Backend

## Getting Started

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/I-am-vishalmaurya/Django_Store_Backend
$ cd Django_Store_Backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pipenv install
$ pipenv shell
```

Open setting.py and under DATABASES add your Database engine password and also create a admin user using following command.
Import the sql file in your database to get some data in database

Create an admin account by using below code
```
python manage.py createsuperuser
```

Then Run the following code
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.
