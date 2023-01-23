## DESCRIPTION
    1. A recipe viewing website 
    2. Created using django
    3. For cashing redis is used
## Features

- View various recipes
- View recipes by categories
- Search for a recipe with its name
- Fast search reasult since cashing is used
- Upload/Delete/Edit recipe from admni panel


## Tech Stack

**Client Side:** HTML, SCSS, TailwindCSS

**Server Side:** Django, Redis


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG = TRUE`

`SECRET_KEY = 'django-insecure-n3&_0olq3#0a33sq3xxs@1jsbf5kccbj-8-!a07bhnh^#m@l2k'`

## Installation

Create a folder and open terminal and install this project by
command 
```bash
git clone https://github.com/Mr-Atanu-Roy/RecipeBook

```
or simply download this project from https://github.com/Mr-Atanu-Roy/RecipeBook

In project directory Create a virtual environment(say env)

```bash
  virtualenv env

```
Activate the virtual environment

For windows:
```bash
  env\Script\activate

```
Install dependencies
```bash
  pip install -r requirements.txt

```
To migrate the database run migrations commands
```bash
  py manage.py magemigrations
  py manage.py migrate

```

Create a super user
```bash
  py manage.py createsuperuser

```
And add some records(recipe) from admin panel.

To run the project in localserver
```bash
  py manage.py runserver

```
Then go to http://127.0.0.1:8000 in your browser to see the project
## Author

- [@Mr-Atanu-Roy](https://www.github.com/Mr-Atanu-Roy)

