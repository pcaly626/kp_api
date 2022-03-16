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
Inside the kp_api/settings.py file there is a variable called INSTALLED_APPS. This variable should already exist in settings.py. Here add the name of the new app. 
`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

Create a Hello World App.

1. Use Django's command line interface to generate a app

`python manage.py startapp helloworld`

2. There will be a new directory called `helloworld`

3. Here create a file called `urls.py` and add this content inside

`
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
`

4. Now add the html file. 

`
mkdir templates
mkdir templates/helloworld
touch templates/helloworld/index.html
`
and add this HTML the index.hmtl

`
<html><body><h1>Hello World</h1></body></html>
`

Save these files

5. Create a index function to render the new html webpage

`
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'helloworld/index.html')
`

6. Install helloworld app to the django project

In config/settings.py add an entry to the `INSTALLED_APPS` variable

`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'helloworld',
]`

7. Add a basename for helloworld app for project

Navigate to config/urls.py and add a unique basename to the urlpatterns variable

`
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('hello/', include('helloword.urls')),
]
`

8. Try it out!

In a browser input the following address and a webpage with Hello World should render

`http://127.0.0.1:8000/hello/`


## Lesson 4 - Models

1. create a new app called `sinapore_districts`
 
2. There will be a new app. Inside go to the `models.py` file and create this model,

`class SinaporeDistrict(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    population = models.IntegerField()`

3. Add a url and view

These will be a placeholder for a future view in the next lesson.

a. Here create a file called `urls.py` and add this content inside

`
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
`
b. Create a index function to render the new html webpage

`
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return JsonResponse({'test':True})
`

4. Add this app to the project like the last lesson 

a. Install helloworld app to the django project

In config/settings.py add an entry to the `INSTALLED_APPS` variable

`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    'helloworld',
    'singapore_districts',
]`

b. Add a basename for helloworld app for project

Navigate to config/urls.py and add a unique basename to the urlpatterns variable

`
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('hello/', include('helloword.urls')),
    path('hello/', include('singapore_districts.urls')),
]
`
5. Migrate the Model to the database

Using Django's command line interface (CLI) there are 2 commands that will create the table in the database.

`python manage.py makemigrations singapore_districts`

This will prepare our model to be added to the database

`python manage.py migrate singapore_districts`

This will create the table in the database

6. Check the table

Django has a adminstrator page to handle database tables. First we need to create a superuser to access the table. 

`python manage.py createsuperuser`

Follow the prompts. Then navigate to the admin link. 

`127.0.0.1:8000/admin`

Type in the credientials for the superuser and view the Signapore District table 

## Lesson 5 - Get Data from Views

 - populate the database using a script 
 - create a view that returns the data. 
## Lesson 5 - Connecting to a Exteranl API
## Lesson 6 - Rendering Data
