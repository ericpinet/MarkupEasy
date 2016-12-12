# MarkupEasy
Markup Language Online Editor

[http://markupeasy.ddns.net](http://markupeasy.ddns.net)



git clone https://github.com/ericpinet/MarkupEasy.git MarkupEasy

cd MarkupEasy

virtualenv django-env

source django-env/bin/active

pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver



-- deploy

sudo apt-get install apache2-prefork-dev

sudo apt-get install python-dev

http://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html


-- update

git clone 

git pull 

git reset --hard origin/master

sudo python manage.py collectstatic
