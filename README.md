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
    
4. Open `127.0.0.1:8000` in a web browser to confirm Django started correctly


## Lesson 2 - Creating a Django App

1. Create a directory called `apps` in the project. This will contain all of our code for this course. 
2. Inside the apps directory create the backend app:

    `python ../manage.py startapp districts_api`

This generates several files to build the app. 

    apps/
        districts_api/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            urls.py
            views.py

    
2. Add new app to project in `settings.py`
Inside the kp_api/settings.py file there is a variable called INSTALLED_APPS. This variable should already exist in settings.py. Here add the name of the new app. 


    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'apps.districts_api'
    ]

3. Add app endpoint to project's `urls.py`

kp_api/urls.py contains the paths to other apps avaliable from the web browser. Add a path to the urlpatterns:

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('apps.districts_api.urls')),
    ]

## Lesson 3 - Views

Create a Hello World App.

1. Use Django's command line interface to generate a app

`python ../manage.py startapp helloworld`

    apps/
        districts_api/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            urls.py
            views.py
        helloworld/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            urls.py
            views.py

2. There will be a new directory called `helloworld`

3. Here create a file called `urls.py` and add this content inside


    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index)
    ]


4. Now create the html file. 


    mkdir templates
    mkdir templates/helloworld
    touch templates/helloworld/index.html

add HTML the index.hmtl and save.

5. Create an index function to render the new html webpage


    from django.shortcuts import render
    
    def index(request):
        return render(request, 'helloworld/index.html')


6. Install helloworld app to the django project

In config/settings.py add an entry to the `INSTALLED_APPS` variable


    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'apps.districts_api',
        'apps.helloworld',
    ]

7. Add a basename for helloworld app for project

Navigate to config/urls.py and add a unique basename to the urlpatterns variable


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('apps.districts_api.urls')),
        path('hello/', include('apps.helloword.urls')),
    ]


8. Try it out!

In a browser input the following address and a webpage with Hello World should render

`http://127.0.0.1:8000/hello/`


## Lesson 4 - Models

1. Go inside the backend app to the `models.py` file and add this code,


    class SinaporeDistrict(models.Model):
        name = models.CharField(max_length=50)
        year = models.CharField(max_length=4)
        population = models.IntegerField()

3. Add a url and view

These will be a placeholder for a future view in the next lesson.

a. Here create a file called `urls.py` and add this content inside


    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index)
    ]

b. Create an index function to render the new html webpage


    from django.shortcuts import render
    from django.http import JsonResponse
    
    def index(request):
        return JsonResponse({'test':True})


4. Migrate the Model to the database

Using Django's command line interface (CLI) there are 2 commands that will create the table in the database.

`python manage.py makemigrations singapore_districts`

This will prepare our model to be added to the database

`python manage.py migrate singapore_districts`

This will create the table in the database

5. Check the table

Django has a administrator page to handle database tables. First we need to create a superuser to access the table. 

`python manage.py createsuperuser`

Follow the prompts. Then navigate to the admin link. 

`127.0.0.1:8000/admin`

Type in the credentials for the superuser and view the Singapore District table 

## Lesson 5 - Get Data from Views

Now that the model is created there needs to be data added. 

1. Using a population script.
Sample data will be located in the root directory. In the *root* of the directory create `populate_districts.py` then add this to the contents.


    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    import django
    django.setup()

    from test_data.data_male import data_male
    from test_data.data_female import data_female
    from apps.districts_api.models import SinaporeDistrict


    def add_data(data_set):
        for year in data_set:
            for data in data_set[year]:
                district = SinaporeDistrict.objects.create(
                    year=year,
                    name=data['name'],
                    population=data['value']
                )
                district.save()


    if __name__ == '__main__':
        add_data(data_male)
        add_data(data_female)

Now run the script 
`python populate_districts.py`

2. Verify Data is now in the database by navigating to the Django admin portal.

3. Update the view and Url

district_api.views

    from django.shortcuts import render
    from django.http import JsonResponse
    from .models import SingaporeDistrict


    def index(request, id):
        district = SingaporeDistrict.objects.get(id=id)
        return JsonResponse({'name': district.name, 'population': district.population, 'year': district.year})

district_api.urls

    from django.urls import path
    from . import views

    urlpatterns = [
        path('<int:id>', views.index),
    ]

The url for district_api will take a parameter for the id of a model.

`127.0.0.1:8000/api/<id>` an example `127.0.0.1:8000/api/1`

## Lesson 6 - Rendering Data to the Frontend

Now that the backend is created we will look at creating an asynchronous call to our endpoint. In this scenario there are a few preparation steps.
First install a python package `pip install django-cors-headers`. This will allow us to call our web own web domain. Below is a link 
that goes into detail why this is necessary. 

[CORS in 100 Seconds](https://www.youtube.com/watch?v=4KHiSt0oLJ0)

Now replace the `config/settings.py` file's content with the following.

"""
Django settings for kp_api project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

    from pathlib import Path
    import os, json
    from config.keys import keys
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    
    
    
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
    
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = keys['secret']
    
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    
    ALLOWED_HOSTS = ['*']
    
    
    # Application definition
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
       'corsheaders', 
        'apps.frontend',
        'apps.backend',
        'apps.helloworld',
        'apps.districts_api'
    ]
    
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]
    
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]
    
    CORS_ALLOW_METHODS = [
    'GET',
    ]
    
    ROOT_URLCONF = 'config.urls'
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    
    WSGI_APPLICATION = 'config.wsgi.application'
    
    
    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        }
    }
    
    
    # Password validation
    # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
    
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]
    
    
    # Internationalization
    # https://docs.djangoproject.com/en/3.1/topics/i18n/
    
    LANGUAGE_CODE = 'en-us'
    
    TIME_ZONE = 'UTC'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/
    MEDIA_ROOT = '/media/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        ('frontend', os.path.join(BASE_DIR, 'static', 'frontend')),
        ('helloworld', os.path.join(BASE_DIR, 'static', 'helloworld'))
    ]

Added settings 

### Install corsheaders 
    
    INSTALLED_APPS = [
        ...
       'corsheaders', 
     ...
    ]

### Install Middleware

    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]

### Add CORS variables for Django
This is for the local domain

     CORS_ALLOWED_ORIGINS = [
            "http://localhost:8000",
            "http://127.0.0.1:8000",
        ]

This is for the request method to allow
    
    CORS_ALLOW_METHODS = [
    'GET',
    ]

### Add Helloworld Static files directory

    STATICFILES_DIRS = [
            ...
            ('helloworld', os.path.join(BASE_DIR, 'static', 'helloworld'))
        ]

Create a directory *static/helloworld/js*. Here assets for our webpage will be stored such as images, css, scss and js files.
Create a file called *population.js* add this code to the file. 

    async function get_singapore_data(){
        let response = await fetch('http://localhost:8000/pop/1',{method:"GET",headers:{'Content-Type':'application/json'}})
        const data = response.json()
        return data;
    }

    get_singapore_one_data().then( data => {
        document.querySelector('#district').append(data.name)
        document.querySelector('#population').append(data.population)
    })

Here is a video that explains what is happening with Asychronous functions.

[Video on Javascript Event loop and Asynchronous functions](https://www.youtube.com/watch?v=EI7sN1dDwcY)


Then go to helloworld's html file and replace the contents with this:

    {% load static %}
    <html>
        <body>
            <h1 id="district"></h1>
            <p id="population"></p>
            <script src="{% static 'helloworld/js/population.js' %}" type="text/javascript"></script>
        </body>
    </html>

Restart the django server and load the page `http://localhost:8000/hello/`. Now the data from the backend will display on the website. 
## Lesson 7 - Connecting to an External API

