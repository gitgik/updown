# updown [![Build Status](https://travis-ci.org/gitgik/updown.svg?branch=develop)](https://travis-ci.org/gitgik/updown)  [![Coverage Status](https://coveralls.io/repos/github/gitgik/updown/badge.svg?branch=develop)](https://coveralls.io/github/gitgik/updown?branch=develop)

A RESTful file management API.


## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/gitgik/updown.git
    ```

* Set the environment variables, specifically the SECRET_KEY
    ```bash
        $ export SECRET_KEY="<my-own-secret>"
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd updown
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Create the updown postgres database to work with:
        ```bash
            $ psql -c "CREATE DATABASE updown;" -U posgres 
        ```
        If you love using the createdb utility provided by Postgres, then
        simply run **`createdb updown`** on your terminal

        After doing this, ensure you set the DATABASE_URL env variable as follows:
        ```bash
            $ export DATABASE_URL="postgresql://localhost:5432/updown"
        ```
    5. Make those migrations work
    ```bash
        $ python manage.py makemigrations
        $ python manage.py migrate
    ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/files/
    ```
