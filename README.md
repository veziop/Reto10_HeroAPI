# Reto10_HeroAPI

## Introduction
This proyect is a simple task for a Django Backend Bootcamp at [Geekshubs Accademy](https://geekshubsacademy.com). It is a REST API built with Django Rest Framework. In this API the user can
create, read, update or delete objects representing famous comicbook superheroes.

## Author
Sole author: Valentin Piombo - valenp97@gmail.com - www.github.com/veziop

## Using the API
First, position the terminal at the root directory (containing 'apihero - db.sqlite3 - manage.py - RETOHERO) and run the server with: <br><br>
```python manage.py runserver```

<br>Then open your browser at "[http://127.0.0.1:8000/hero/](http://127.0.0.1:8000/hero/)" to see the current list of superheros. 
This list is very brief, add more by filling the form at the bottom of the page and click **POST**.

<br>To update, partially update or delete an entry go to its endpoint 'hero/<pk>' where pk is it's ID and click on **DELETE**. Alternatively click on 
Raw Data to edit the JSON input and finally click **PUT** to update, or **PATCH** to partially update.

------------------------------

## Models
The only model in this project is Hero, and it has three attributes:
* id - Big Int Primary Key
* name - Charfield (the name of the superhero eg: Superman, Wolverine)
* alias - Charfield (the superhero's secret identity)

## Serializers
Only serializer is HeroSerializer, that is set up to be in charge of serializing the model Hero's data.

## Viewsets
Again, only one ViewSet to manage all CRUD operations. This viewset is called HeroViewSet and it inherits from ModelViewSet

## URLConfig
Only one urlpatter is set up, the endpoint 'hero/'. The ModelViewSet helps with the default routes 'hero/<int:pk>/' for operations regarding
one specific object.

## Moving foreward
This project is very rudimentary, so next projects should include very important REST components like permissions, JWT, tests, authentication, etc. 
