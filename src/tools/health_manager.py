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
from pathlib import Path
from datetime import date

# Third party modules
import aiofiles

# local modules
from ..config.setup import config
from ..api.models import ResourceModel, HealthResponseModel

# Constants
CERT_EXPIRE_FILE = (
        Path(__file__).parent.parent.parent / 'certs' / 'expire-date.txt'
)
""" File containing certificate expiry date. """


# ---------------------------------------------------------
#
async def _get_certificate_remaining_days() -> int:
    """ Return SSL certificate remaining valid days.

    Will return 0 if the cert expires-date file is missing,
    or an invalid ISO 8601 date format (YYYY-MM-DD) is found.

    :return: Remaining valid days.
    """
    try:
        async with aiofiles.open(CERT_EXPIRE_FILE, mode='r') as cert:
            raw_date = await cert.read()

        remaining_days = date.fromisoformat(raw_date) - date.today()
        return remaining_days.days

    except (EnvironmentError, ValueError):
        return 0


# ---------------------------------------------------------
#
def _get_certificate_status(remaining_days: int) -> List[ResourceModel]:
    """ Return SSL certificate validity status.

    :return: Certificate validity status.
    """
    return [ResourceModel(name='Certificate.valid',
                          status=remaining_days > 0)]


# ---------------------------------------------------------
#
async def get_health_status() -> HealthResponseModel:
    """ Return Health status for used resources.

    :return: Service health status.
    """
    resource_items = []
    days = await _get_certificate_remaining_days()
    resource_items += _get_certificate_status(days)
    total_status = (all(key.status for key in resource_items)
                    if resource_items else False)

    return HealthResponseModel(status=total_status,
                               version=config.version,
                               name=config.service_name,
                               resources=resource_items,
                               cert_remaining_days=days)
