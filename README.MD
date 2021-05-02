## CLONE AMAZON USING DJANGO

### GITHUB REPOSITORY

https://github.com/gurnitha/django-clone-amazon-renewed

### 1. BASICS SETUP

#### 1.1.1 Create project folders

        ... DJANGO-CLONE-AMAZON-RENEWED> mkdir src
        ... DJANGO-CLONE-AMAZON-RENEWED> mkdir src
        ... DJANGO-CLONE-AMAZON-RENEWED> cd src
        ... DJANGO-CLONE-AMAZON-RENEWED\src> touch .gitignore
        ... DJANGO-CLONE-AMAZON-RENEWED\src> touch README.md
        ... DJANGO-CLONE-AMAZON-RENEWED\src> git init
        ... DJANGO-CLONE-AMAZON-RENEWED\src> git add .
        ... DJANGO-CLONE-AMAZON-RENEWED\src> git commit -m "1.1.1 Create project folders"
        ... DJANGO-CLONE-AMAZON-RENEWED\src> tree /f
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

        ... DJANGO-CLONE-AMAZON-RENEWED\src> python -m venv venv3932
        modified:   .gitignore
        modified:   README.MD

### 4. INSTALL DJANGO

#### 4.1.5 Install django v3.2

        ...DJANGO-CLONE-AMAZON-RENEWED\src> .\venv3932\scripts\activate
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
