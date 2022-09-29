# JWT SETTINGS
SECRET_KEY = 'dafsdgsdf1234r34we21eewdsfqrwetwert'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# DATABASE
DB_URL = 'postgresql://postgres:addr1234@localhost:5432/todoapp'

INSTALLED_APPS = [
    'account',
]

API_VERSION = "1"

try:
    from settings_local import *
except ImportError:
    pass
