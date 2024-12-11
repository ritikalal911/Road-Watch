# RoadWatch

A comprehensive web application for road monitoring and management built with Django and MySQL.

## Overview

RoadWatch is a web-based platform designed to help monitor and manage road conditions, providing an efficient system for tracking and maintaining road infrastructure.

## Prerequisites

- Python 3.8 or higher
- MySQL Server
- MySQL Workbench (optional, recommended for database management)
- Visual Studio Code (optional)

## Installation

### 1. Project Setup

```bash
# Clone the repository
git clone https://github.com/ritikalal911/Road-watch.git
cd Road-watch

# Create and activate virtual environment
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```


### 2. Django Configuration

1. Open `myproject/settings.py`
2. Configure database settings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'roadwatch',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Initialize Application

```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Usage

1. Access the application at `http://127.0.0.1:8000`
2. Login to the admin panel at `http://127.0.0.1:8000/admin` using superuser credentials

## Troubleshooting

If you encounter the error 'mysql' is not recognized:
1. Verify MySQL installation
2. Check if MySQL is added to system PATH
3. Try using the full path to MySQL executable

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Project Link: [https://github.com/ritikalal911/Road-watch](https://github.com/ritikalal911/Road-watch)
