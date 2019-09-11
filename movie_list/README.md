How to run the app:

It's recommended to create a virtualenv to install the project dependencies. I use `virtualenvwrapper` for this.
- clone the repo
- `$ cd movie_list`
- `$ pip3 install -r requirements.pip`
- `$ cd movies`
- `$ python manage.py migrate`
- `$ python manage.py runserver`
- in a browser, navigate to `http://127.0.0.1:8000/movies/`