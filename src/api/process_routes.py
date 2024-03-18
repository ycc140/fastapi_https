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

# BUILTIN modules
import asyncio
from uuid import uuid4
from typing import Annotated

# Third party modules
from fastapi import Depends, APIRouter, Body, HTTPException

# local modules
from ..tools.security import validate_authentication
from .documentation import process_request_body_example
from .models import ProcessResponseModel, ProcessingError

# Constants
ROUTER = APIRouter(prefix="/v1/process", tags=["Process endpoints"])
""" Process API endpoint router. """


# ---------------------------------------------------------
#
async def _fake_processing(payload: dict) -> bool:
    """ Fake process payload."""
    await asyncio.sleep(1.0)
    return payload.get('status') == 'SUCCESS'


# ---------------------------------------------------------
#
@ROUTER.post('', response_model=ProcessResponseModel,
             responses={500: {"model": ProcessingError}},
             dependencies=[Depends(validate_authentication)])
async def process_payload(payload: Annotated[
    dict,
    Body(openapi_examples=process_request_body_example)
]) -> ProcessResponseModel:
    """**Payload processing.**"""

    if await _fake_processing(payload):
        return ProcessResponseModel(status='SUCCESS', id=f'{uuid4()}')

    raise HTTPException(status_code=500, detail=ProcessingError().detail)
