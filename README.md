# kp_api

App to connect various apis and render to a Dashboard

# Installation

- backend
    - pip install virtualenv
    - virtualenv venv
    - pip install -r requirements.txt
- frontend
   - npm i 
   - npm run dev

# Learning 

Reference [Django documentation](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

## Lesson 1 - Creating a Django server

Pre-requisite before starting a new project create a virtual python environment. This will ensure the current project will not conflict with others on your machine. [Try this guide](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b).

1. Install Django based on your OS ( either through the git repository or pip install django )

    `python -m pip install Django`
    
2. Use Django Admin to start a project

    `django-admin startproject kp_api`
    
3. Start Server

    `python manage.py runserver`
    
4. Open 127.0.0.1:8000 in a web browser to confirm Django started correctly


## Lesson 2 - Creating a Django App

1. Inside the root of the project create the app

    `python manage.py startapp backend`

This generates several files to build the app. 

`backend/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py`
    
2. Add new app to project in `settings.py`
Inside the kp_api/settings.py file there is a variable called INSTALLED_APPS. Here add the name of the new app. 

`INSTALLED_APPS = [
    'backend'
]`

3. Add app endpoint to project's `urls.py`

kp_api/urls.py contains the paths to other apps avaliable from the web browser. Add a path to the urlpatterns:

from django.contrib import admin
from django.urls import include, path

`urlpatterns = [
    path('api/', include('backend.urls')),
    path('admin/', admin.site.urls),
]`

## Lesson 3 - Views
## Lesson 4 - Models
## Lesson 5 - Connecting to a Exteranl API
## Lesson 6 - Rendering Data
