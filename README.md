# testsmartquick

INSTALLATION W
1. Install Python 3.9.2 version
2. Create virtual environment:
  - python -m venv project-name
3. Activate virtual environment:
  - in virtual environment directory "\project-name\Scripts" run command activate
4. Install Django in virtual environment:
  - pip install Django==3.2.3
5. Run the following commands to start:
  - pip install djangorestframework
  - pip install django-rest-auth
  - pip install django-allauth
  - pip install django-import-export
  - python manage.py migrate
  - python manage.py runserver

ENDPOINTS USER
- Register User

URL:
/auth/registration/

Method:
POST

Data Params:
{
    "username": "",
    "email": "",
    "password1": "",
    "password2": ""
}

- Login User

URL:
/auth/login/

Method:
POST

Data Params:
{
    "username": "",
    "password": ""
}

ENDPOINTS CRUDS

Headers in all endpoints:
Authorization 
* Example: [{"key":"Authorization","value":"token 7344df6f294c960ed63031813658922424cd18d1"}]

- Show Clients

URL:
/api/clients/

Method:
GET

URL Params 
Optional:
id=[integer]

- Create Clients

URL:
/api/clients/

Method:
POST

Data Params:
{
    "document": "",
    "first_name": "",
    "last_name": "",
    "email": ""
}

- Update Clients

URL:
/api/clients/id/

Method:
PUT

URL Params 
Required:
id=[integer]

Data Params:
{
    "document": "",
    "first_name": "",
    "last_name": "",
    "email": ""
}

- Delete Clients

URL:
/api/clients/id/

Method:
DELETE

URL Params 
Required:
id=[integer]

- Show Products

URL:
/api/products/

Method:
GET

URL Params 
Optional:
id=[integer]

- Create Products

URL:
/api/products/

Method:
POST

Data Params:
{
    "name": "",
    "description": "",
    "price": ""
}

- Update Products

URL:
/api/products/id/

Method:
PUT

URL Params 
Required:
id=[integer]

Data Params:
{
    "name": "",
    "description": "",
    "price": ""
}

- Delete Products

URL:
/api/products/id/

Method:
DELETE

URL Params 
Required:
id=[integer]

- Show Bills

URL:
/api/bills/

Method:
GET

URL Params 
Optional:
id=[integer]

- Create Bills

URL:
/api/bills/

Method:
POST

Data Params:
{
    "company_name": "",
    "nit": "",
    "code": "",
    "client": null
}

- Update Bills

URL:
/api/bills/id/

Method:
PUT

URL Params 
Required:
id=[integer]

Data Params:
{
    "company_name": "",
    "nit": "",
    "code": "",
    "client": null
}

- Delete Bills

URL:
/api/bills/id/

Method:
DELETE

URL Params 
Required:
id=[integer]

- Show BillsProducts

URL:
/api/billsProducts/

Method:
GET

URL Params 
Optional:
id=[integer]

- Create BillsProducts

URL:
/api/billsProducts/

Method:
POST

Data Params:
{
    "bill": null,
    "product": null
}

- Update BillsProducts

URL:
/api/billsProducts/id/

Method:
PUT

URL Params 
Required:
id=[integer]

Data Params
{
    "bill": null,
    "product": null
}

- Delete BillsProducts

URL:
/api/billsProducts/id/

Method:
DELETE

URL Params 
Required:
id=[integer]

