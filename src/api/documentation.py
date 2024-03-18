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

process_request_body_example = {
    "ok": {
        "summary": "success",
        "value": {"status": "SUCCESS"}},
    "error": {
        "summary": "failure",
        "value": {"status": "FAILURE"}}
}
""" OpenAPI process request body choice values. """
