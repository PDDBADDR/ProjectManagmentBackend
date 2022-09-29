import importlib

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import settings

fastapi_app = FastAPI()

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# INCLUDE ALL ROUTERS
for app in settings.INSTALLED_APPS:
    app_api = importlib.import_module(f'{app}.api.v{settings.API_VERSION}')
    router = app_api.router
    fastapi_app.include_router(router)