import importlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings
from settings import DB_URL

SQLALCHEMY_DATABASE_URL = DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# INCLUDE ALL MODELS FOR ALEMBIC
for app in settings.INSTALLED_APPS:
    models = importlib.import_module(f'{app}.models', '*')
