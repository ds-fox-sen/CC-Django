# From Python Crash Course Django project


Example of Django project to manage an online journal system that lets user keep track of information on learned topics

**Uses:**
- Django
- virtualenv  


### environment setup
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

### django setup
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
