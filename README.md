SamarAouadi 

# Django Project with GraphQL @SamarAouadi

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Django 5.1](https://img.shields.io/badge/Django-5.1-brightgreen)](https://www.djangoproject.com/)

Django application with a GraphQL API for image management and email smtp notifications.

## 📋 Requirements
- Python 3.8+
- PostgreSQL
- SMTP Email Configuration (e.g., Gmail, Outlook, etc.)
- Git

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AouadiSamar/WOrkProjectDjango_samar.git
cd WOrkProjectDjango_samar
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure SMTP (Example for Gmail)
Edit the settings in your `settings.py` file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your.email@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your_app_password'  # App password for Gmail
DEFAULT_FROM_EMAIL = 'Notification System <your.email@gmail.com>'
```

### 5. Configure PostgreSQL Database
In `settings.py`, configure the database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'workprojectdb',
        'USER': 'postgres',
        'PASSWORD': 'your_password',  # Replace with your password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

For test run python manage.py test
