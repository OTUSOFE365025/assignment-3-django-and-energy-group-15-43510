# Assignment 3 — Django and Energy (Group 15-43510)

This project demonstrates how to use Django’s ORM (Object-Relational Mapper) both in a **stand-alone script** (`main.py`) and as a **web application** with templates, views, and URLs.  
It was created for the Ontario Tech Software Engineering course **SOFE 3650 – Software Architecture and Design**.

---

## Overview

The goal of this assignment is to:
1. Build and interact with a database model using Django’s ORM.
2. Create a simple Django web interface that simulates a cash register or product scanner.
3. Write a short reflection on energy efficiency as a software quality attribute.


## Requirements

- Python 3.10 or newer  
- Django 5.x (or compatible)  
- SQLite 3 (default database)

Install Django with:
```bash
pip install django
````

## Project Structure

```
assignment-3-django-and-energy-group-15-43510/
├── db/
│   ├── __init__.py
│   ├── models.py          # Product model definition
│   ├── urls.py            # App routing
│   ├── views.py           # Handles form and rendering
│   └── templates/
│       └── scan.html      # Web UI for product scanning
├── main.py                # Stand-alone ORM script
├── manage.py              # Django project manager
├── settings.py            # Database and template configuration
├── urls.py                # Root URL router
└── db.sqlite3             # SQLite database
```

---

## How to Run

### 1️⃣ Migrate the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2️⃣ Run the stand-alone ORM script

```bash
python main.py
```

This seeds the database and allows UPC scanning in the terminal.

### 3️⃣ Start the web server

```bash
python manage.py runserver
```

Then open your browser at
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
to use the simple scan page.

---

## Example Workflow

**Console output (`main.py`):**

```
Enter a UPC to scan: 1111
Product found: Milk — $3.49
```

**Web interface (`scan.html`):**

```
Scan a Product
[UPC input box] [Scan button]
Product: Milk
Price: $3.49
```

