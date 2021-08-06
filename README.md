# Django_Store_Backend

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/I-am-vishalmaurya/Django_Store_Backend
$ cd Django_Store_Backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Open setting.py and under DATABASES add your Database engine password and also create a admin user using following command.
```
python manage.py createsuperuser
```

Then Run the following code
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.
