# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::

    $Repo: fastapi_https
  $Author: Anders Wiklund
    $Date: 2024-03-18 15:47:18
     $Rev: 4
"""

# BUILTIN modules
from typing import List

# Third party modules
from pydantic import BaseModel, UUID4


# -----------------------------------------------------------------------------
#
class HealthStatusError(BaseModel):
    """ Define OpenAPI documentation for a http 500 exception (INTERNAL_SERVER_ERROR).

    :ivar detail: Error detail text.
    """
    detail: str = "HEALTH: resource(s) are down"


class ProcessingError(BaseModel):
    """ Define OpenAPI documentation for a http 500 exception (INTERNAL_SERVER_ERROR).

    :ivar detail: Error detail text.
    """
    detail: str = "Celery task processing failed"


# -----------------------------------------------------------------------------
#
class ResourceModel(BaseModel):
    """ Representation of a health resources response.

    :ivar name: Resource name.
    :ivar status: Resource status
    """
    name: str
    status: bool


# -----------------------------------------------------------------------------
#
class HealthResponseModel(BaseModel):
    """ Representation of a health response.

    :ivar name: Service name.
    :ivar status: Overall health status
    :ivar version: Service version.
    :ivar resources: Status for individual resources.
    :ivar cert_remaining_days: Remaining SSL/TLS certificate valid days.
    """
    name: str
    status: bool
    version: str
    cert_remaining_days: int
    resources: List[ResourceModel]


# -----------------------------------------------------------------------------
#
class ProcessResponseModel(BaseModel):
    """ Define OpenApi model for API process_payload responses.

    :ivar id: Task ID for the current job.
    :ivar status: Response status (FAILURE|SUCCESS).
    """
    id: UUID4
    status: str
