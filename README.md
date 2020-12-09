# diveShop

Install DJANGO

Run CMD as Administrator

>> pip install Django==X.X.X

To check the version, go to the CMD

>> python import django django.VERSION

To create a project in Django, first go to DjangoProjects folder:

>> django-admin startproject "Name of the project"

>> cd "Name of the project"

>> manage.py help (for information)

>> python manage.py migrate

To run the Python server:

>> python manage.py runserver

To create an app (BBDD)

>> django-admin startproject "Name of the APP"

>> cd "Name of the project"

>> python manage.py startapp "name of the APP"

To check if there is issue

>> python manage.py check "name of the APP"

To create the BBDD

>> python manage.py makemigrations

>> python manage.py sqlmigrate "Name of the APP" "Number of the migrations got it during makemigrations"

>> python manage.py migrate

To manipulate the BBDD

>> python

>> from "nameofthemodel".models import Table1

>> obj1 = Table1(name='xxx', section='xxx', price=yyy)

>> obj1.save()

To modify a value

>> obj1.price = yyy

>> obj1.save()

>> objX=Table1.objects.get(id=1)

>> objX.delete()
