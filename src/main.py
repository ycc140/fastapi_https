# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::
    $Repo: fastapi_https
  $Author: Anders Wiklund
    $Date: 2024-03-18 15:01:47
     $Rev: 1
"""

# Third party modules
from fastapi import FastAPI

# local modules
from .config.setup import config
from .api import process_routes, health_route

# ---------------------------------------------------------

# Instantiate the service.
app = FastAPI(
    redoc_url=None,
    title=config.name,
    version=config.version,
)

app.include_router(process_routes.ROUTER)
app.include_router(health_route.ROUTER)
