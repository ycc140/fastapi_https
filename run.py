#!/usr/bin/env python
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

# Third party modules
import uvicorn

if __name__ == "__main__":
    uv_config = {'reload': True,
                 'app': 'src.main:app',
                 'ssl_keyfile': "certs/private-key.pem",
                 'ssl_certfile': "certs/public-cert.pem"}
    uvicorn.run(**uv_config)
