# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class VersionResponseStatus(str, Enum):
    """VersionResponseStatus."""

    STARTING = "STARTING"
    STARTED = "STARTED"
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)