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
import site
from pathlib import Path

# Third party modules
from pydantic_settings import (BaseSettings, SettingsConfigDict)

# Constants
MISSING_ENV = '>>> missing ENV value <<<'
""" Error message for missing values in the .env file. """
MISSING_SECRET = '>>> missing SECRETS file <<<'
""" Error message for missing secrets file. """


# -----------------------------------------------------------------------------
#
class SetupParameters(BaseSettings):
    """ Application configuration parameters. """
    model_config = SettingsConfigDict(env_file_encoding='utf-8',
                                      secrets_dir=f'{site.USER_BASE}/secrets',
                                      env_file=Path(__file__).parent / '.env')

    # Project parameters.
    name: str = MISSING_ENV
    version: str = MISSING_ENV
    service_name: str = MISSING_ENV

    # External resource parameters.
    service_api_key: str = MISSING_SECRET


# ---------------------------------------------------------

config = SetupParameters()
""" Application configuration parameters. """
