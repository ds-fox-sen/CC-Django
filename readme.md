r# From Python Crash Course Django project


Example of Django project to manage an online journal system that lets user keep track of information on learned topics

### Basic logic:

 - Each user can to create a number of topics in their learning log.

 - Each entry they make will be tied to  a topic, and these entries will be displayed as text.
 - The program also stores the timestamp of each entry so we can show users when they made each entry.

**Uses:**
- Django
- virtualenv  


### Environment setup
~~~
# Install virtual environment package.
pip install --user virtualenv

# Create new virtual env.
virtualenv ll_env

# Activate ll_env.
source ll_env/bin/activate

# Deactivate ll_env
deactivate
~~~

### Django setup
~~~~
# Install pip.
pip install Django

# Create new project.
django-admin.py startproject learning_log .

# Create custom Database.
python manage.py migrate

# Run webserver.
python manage.py runserver

# Create infrasture needed to build an app.
python manage.py startapp learning_logs
~~~~

### Django modifing DB data
~~~

# 1: Edit proper models.py file.

# 2: Create migration file.
python manage.py makemigrations <django app name>

# 3: Migrate to database.
python manage.py migrate
~~~
