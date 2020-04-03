"""
def addStudent(request):
    all_schools = School.objects.all() #import school in db after importing School model
    if request.method == "POST":
        form = request.POST
        student = Student()
        student.name = form['name']
        student.registration_number = form['registration_number']
        student.address = form['address']
        student.age = form['age']
        student.parent_mobile = form['parent_mobile']
        student.school = School.objects.get(pk=form['school']) #grab if of the school in the DB
        student.save() #save the details in the database
        
        return redirect('students:student_list') #redirect to the link under urls.py
    
    context = {'all_schools':all_schools}
    
    return render(request,"students/add_student.html",context)
    
===form for abpve function====

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Students</title>
</head>

<body>
    <form action="{% url 'students:add' %}" name="frm_student" method="POST">
        {% csrf_token %}
        <!--Prevents cross site scripting-->
        <label for="name"> Name :</label>

        <input type="text" id="name" name="name" value="">
<br>
        <label for="name"> Registration :</label>

        <input type="text" id="registration_number" name="registration_number" value="">
<br>
        <label for="name"> Address :</label>
        
        <input type="text" id="address" name="address" value="">
<br>
       
        <label for="number">Age :</label>

        <input type="number" id="age" name="age" value="">
<br>
        <label for="parent_mobile"> Parent Mobile :</label>

        <input type="text" id="parent_mobile" name="parent_mobile" value="">
<br>
        <label for="parent_mobile"> School</label>

        <select name="school" id="school">
            {%for school in all_schools%}
            <option value="{{school.id}}">{{school.name}}</option>
            {%endfor%}
        </select>
<br>
        <input type="Submit" value="Save">

    </form>
</body>

</html>


urlpatterns = [
    path('schools/',views.show_schools,name='schools'),
    path('schools/<int:school_id>/',views.show_students,name='school_details'),
]

#dynamic views example

def show_students(request,school_id):
    #school_detail=School.objects.get(pk=school_id) if you want to display school details
    school_student = Student.objects.filter(school=school_id)
    context = {'school_student':school_student}
    return render(request,"schools/details.html",context)


# admin filters example

from django.contrib import admin
from.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','idNumber','mobileNo','pin') #list_display is inbuilt
    search_fields = ('name','idNumber') #seach fields is inbuilt
    
#allow display multiple items on admin page
admin.site.register(Customer,CustomerAdmin)
"""

#rendering a view example
from django.shortcuts import render
from .models import Posts


# Create your views here.
def post_list_view(request):
    post_objects = Posts.objects.all()
    context = {
        'post_objects': post_objects
    }
    return render(request, "posts/index.html", context) #posts/index.html should be under appname/templates/appname/index.html

#==================
python3 manage.py shell
from schools.models import School
School.objects.all()
school = School(name='Upperhill',code='2003',address='Nyeri',no_of_students=10)
school.save()
School.objects.all()

#models example under manage.py

#important codes
sudo apt install python3-pip
sudo apt-get install mysql-client
pip install mysqlclient
source env/bin/activate
python3 manage.py runserver
python3 manage.py startapp transactions
python(3) -m venv env
pip install django
#if the database is ot available during migrations,add this in init.py
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()


class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    no_of_students = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_schools'

#setting up admin example under each module's admin.py

from .models import School
# Register your models here.
admin.site.register(School)

=========

----------------------
Course Prerequisites
----------------------
    - Right Attitude
    - Background in core python programming
    - OOP Basics
    - 


----------------------
Why Django
----------------------

- widely used 

- open source 

- high level, easy to learn and pickup - encourages rapid development and clean design

- allows you to focus on building your app without re-inventing the wheel


MAIN FEATURES
-----------------------------
    - Fast - designed to help developers take apps from concept to completion fast.

    - Secure - Helps developers avoid common security mistakes.

    - Scalable - has ability to quickly and flexibly scale.


- Follows the MVC pattern

Model View Controller


-----------------
Installation
-----------------
1. Check if django is installed

python(3) -m django --version  


if not installed

Create a Virtual Environment
- acts as dependencies to the Python-related projects.

-  self contained or an isolated environment where all the Python-related packages and specific required versions of the projects are kept.

- Older newer versions of python co-work

    a) create project folder (mkdir my_school_project)

        cd to project folder

    b) run command python(3) -m venv env

    NB: Python will not support version 2 after the year 2020.

    c) run command ls - view environment 

    d) activate the environment 

        source env/bin/activate

    e) install django  in the virtual environment

        - pip install django



2. Create a django project

using django-admin startproject

    - django-admin startproject my_bank

    - Project with many files created

    a) cd to newly created folder
    b) run the project with :python3 manage.py runserver 

    or python3 manage.py runserver 8080

    NB: ensure environment is created/activated else you will get a serious error

- Access the website on url & port

NB: repeat the process until you are comfortable


--------------------------------
Folder Structure Explained
--------------------------------
1. my_bank_project/ 

 - root directory - contains project files

2. env
    - Virtual environment folder 

3. my_bank /
    - project name

4. manage.py
  - command utility for interacting with django
  
5. The inner my_bank/ 

    - Python package for the project.
    - Name can be used to import anything inside it (e.g. my_bank.urls).

6. my_bank/__init__.py: 

    - empty file, tells Python that this directory should be considered a Python package.
    
7. my_bank/settings.py:

    - Settings/configuration for the project.
    - e.g DB settings

8. my_bank/urls.py: 
    - The URL declarations for the project;

9. my_bank/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
    - Asynchronous Server Gateway Interface)
    - provide a standard interface between async-capable Python web servers, frameworks, and applications.

    - WSGI provided a standard for synchronous Python apps, 
    - ASGI provides one for both asynchronous and synchronous apps, 
    with a WSGI backwards-compatibility implementation and multiple servers
     and application frameworks.

10. my_bank/wsgi.py: An entry-point for WSGI-compatible web servers to serve

    - WSGI provided a standard for synchronous Python apps, 


------------------------
3. Starting the new Project Module (2 Step)
------------------------
My_Bank 
Customers
Accounts 
Currency

(my_school)
Schools - Define Models, urls, views etc
Students
Subjects


1. python(3) manage.py startapp app_name

    - python3 manage.py startapp customer
    - python3 manage.py startapp accounts
    - python3 manage.py startapp customer
    
    - django can have many apps to the single project where each app serves as single and 
    specific functionality to the particular project.


2. Make our project know about our newly created app 
 
    update the file 
    'my_bank/settings.py' INSTALLED_APP section.


3. Configure DB Connection

Database setup

We use Mysql for this purpose.

if missing mysqlclient run below in virtual env

pip install mysqlclient

SETTINGS Database
-------------------
-     'default':{
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'localhost',
        'PORT':3306,
        'NAME':'codev_django',
        'USER':'root',
        'PASSWORD':'pass'
    }



CREATING MODELS
-------------------

class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100,unique=True)
    id_number = models.CharField(max_length=10)
    admission_date = models.DateField()
    age = models.IntegerField()


    class Meta:
    db_table = 'tbl_customer'
    managed = True #flush or sync db



NB: Object Relational Mapper(ORM)

Making a Migrations
1. python3 manage.py makemigrations

Migrating to the Database ('Also Creates the Database tables')

2. python3 manage.py migrate


NB: Login to database and confirm is tables are created



-------------------
DJANGO ADMIN
-------------------
- Used for content management

/admin url

--------------------
Create a Super user 
--------------------


- python3 manage.py createsuperuser

- enter required details

- Login to the Admin Page

- Make the app modifiable by admin

    - 
    modify admin.py in respective module
    from .models import Account
    # Register your models here.

    # Register your models here.
    admin.site.register(Account)


We build our model Bank based on the previous classes.
------------------------
Functionality 
------------------------
    - A public site that allows customers to access.

    - An admin site that lets the bank staff to add, change, and delete customers.

    - Capture Customers

    - Create Accounts for Customers

    - Assign Currency to Account

    - Allow Cutomer Load Money 

    - Allow Customer to Check Balance

    - Allow Customer Transfer to Another Customer.
