# updown [![Build Status](https://travis-ci.org/gitgik/updown.svg?branch=develop)](https://travis-ci.org/gitgik/updown)

A RESTful file managing API ~ with steroids!


## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```
        $ git clone https://github.com/gitgik/updown.git
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
            $ cd updown
        ```

    2. Create and fire up your virtual environment:
        ```
            $ virtualenv env
            $ source env/bin/activate
        ```
    3. Install the dependencies needed to run the app:
    ```
        $ pip install -r requirements.txt
    ```
    4. Create the updown postgres database to work with:
    ```
        $ psql -c "CREATE DATABASE updown;" -U posgres 
    ```
    If you love using the createdb utility provided by Postgres, then
    simply run **`createdb updown`** on your terminal

    4. Make those migrations work
    ```
        $ python manage.py makemigrations
        $ python manage.py migrate
    ```

* #### Run It
    Fire up the server using this one simple command:
    ```
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/files/
    ```
