# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::

    $Repo: fastapi_https
  $Author: Anders Wiklund
    $Date: 2024-03-19 11:52:28
     $Rev: 5
"""

# BUILTIN modules
from typing import Annotated

# Third party modules
from fastapi import Body

process_body_example = {
    "ok": {
        "summary": "success",
        "value": {"status": "SUCCESS"}},
    "error": {
        "summary": "failure",
        "value": {"status": "FAILURE"}}
}
""" OpenAPI process request body choice values. """

ProcessTypeBodyChoice = Annotated[
    dict,
    Body(openapi_examples=process_body_example)
]
""" Process payload type hint with OpenAPI documentation. """
