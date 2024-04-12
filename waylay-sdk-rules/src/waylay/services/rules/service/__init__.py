# coding: utf-8
"""Waylay rules engine: Service.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

version: 6.5.0

The REST api to manage rule tasks and rule templates in the Waylay platform.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

__version__ = "6.5.0"

from .service import RulesService

PLUGINS = [RulesService]

__all__ = [
    "__version__",
    "RulesService",
]
