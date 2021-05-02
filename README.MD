## CLONE AMAZON USING DJANGO

### GITHUB REPOSITORY

https://github.com/gurnitha/django-clone-amazon-renewed

### 1. BASICS SETUP

#### 1.1.1 Create project folders

        ...\DJANGO-CLONE-AMAZON-RENEWED> mkdir src
        ...\DJANGO-CLONE-AMAZON-RENEWED> mkdir src
        ...\DJANGO-CLONE-AMAZON-RENEWED> cd src
        ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch .gitignore
        ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch README.md
        ...\DJANGO-CLONE-AMAZON-RENEWED\src> git init
        ...\DJANGO-CLONE-AMAZON-RENEWED\src> git add .
        ...\DJANGO-CLONE-AMAZON-RENEWED\src> git commit -m "1.1.1 Create project folders"
        ...\DJANGO-CLONE-AMAZON-RENEWED\src> tree /f
            ...
            E:.
                .gitignore
                README.MD
        new file:   .gitignore
        new file:   README.MD

### 2. CREATE REMOTE (GITHUB) REPOSITORY

#### 2.1.2 Create a new github repository

        https://github.com/gurnitha/django-clone-amazon-renewed
        modified:   README.MD

#### 2.2.3 Modified README.md

### 3. CREATE VIRTUAL ENVIRONMENT

#### 3.1.4 Create venv named it 'venv3932'

        ...\DJANGO-CLONE-AMAZON-RENEWED\src> python -m venv venv3932
        modified:   .gitignore
        modified:   README.MD

### 4. INSTALL DJANGO

#### 4.1.5 Install django v3.2

        ...\DJANGO-CLONE-AMAZON-RENEWED\src> .\venv3932\scripts\activate
        (venv3932) ...DJANGO-CLONE-AMAZON-RENEWED\src> python -m pip install django==3.2
        (venv3932) ...DJANGO-CLONE-AMAZON-RENEWED\src> python -m pip install --upgrade pip
        modified:   README.MD

### 5. CREATING DJANGO PROJECT AND APP

#### 5.1.6 Create django project called 'config'

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> django-admin startproject config .
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py runserver
        modified:   README.MD
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 5.2.7 Create django app called 'main'

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir app
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir app/main
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py startapp main app/main
        modified:   README.MD
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py

#### 5.3.7 Modified README.md

#### 5.4.8 Install django app 'main' to django project 'config'

        modified:   README.MD
        modified:   app/main/apps.py
        modified:   config/settings.py
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py check
        System check identified no issues (0 silenced).
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py runserver

#### 5.5.8 Modified README.md

### 6. CREATE DUMMY PAGES

#### 6.1.9 Create Home and About pages

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir templates\main
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch templates\main\home.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch templates\main\about.html
        modified:   README.MD
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/main/about.html
        new file:   templates/main/home.html

#### 6.2.10 Linking the pages

        modified:   README.MD
        modified:   templates/main/about.html
        modified:   templates/main/home.html

#### 6.3.11 Using template inheritance (base template)

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch templates\base.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir templates\main\shared
        modified:   README.MD
        new file:   templates/base.html
        modified:   templates/main/about.html
        modified:   templates/main/home.html
        new file:   templates/main/shared/navbar.html

#### 6.4.12 Adding semi-dynamic head page title

        modified:   README.MD
        modified:   templates/base.html
        modified:   templates/main/about.html
        modified:   templates/main/home.html

### 7. ADBORD (ADMIN DASHBOARD)

#### 7.1.13 Create django app called 'adbord'

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir app/adboard
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py startapp adbord app/adboard
        modified:   README.MD
        new file:   app/adboard/__init__.py
        new file:   app/adboard/admin.py
        new file:   app/adboard/apps.py
        new file:   app/adboard/migrations/__init__.py
        new file:   app/adboard/models.py
        new file:   app/adboard/tests.py
        new file:   app/adboard/views.py

#### 7.2.14 Register django app 'adbord' to django project 'config'

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir app/adboard
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py startapp adboard  app/adboard
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> python manage.py check
        System check identified no issues (0 silenced).
        modified:   README.MD
        modified:   app/adboard/apps.py
        modified:   config/settings.py

#### 7.3.15 Create Home page for Adboard and link it with front pages

        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir .\templates\adboard
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> mkdir .\templates\adboard\shared
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch .\templates\adboard\home-adboard.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch .\templates\adboard\shared\navbar-adboard.html
        (venv3932) ...\DJANGO-CLONE-AMAZON-RENEWED\src> touch .\templates\base-adboard.html
        modified:   README.MD
        modified:   app/adboard/views.py
        modified:   config/urls.py
        new file:   templates/adboard/home-adboard.html
        new file:   templates/adboard/shared/navbar-adboard.html
        new file:   templates/base-adboard.html
        modified:   templates/main/shared/navbar.html

#### 7.4.16 re-naming views and path of the adboardHomePage to homePageAdboard

        modified:   README.MD
        modified:   app/adboard/views.py
        modified:   config/urls.py

### 8. ADBOARD - LOG IN AND LOG OUT

#### 8.1.17 Create login page: views, template and path

        modified:   README.MD
        modified:   app/adboard/views.py
        modified:   config/urls.py
        new file:   templates/adboard/login-adboard.html
        modified:   templates/main/shared/navbar.html
