# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class PluginUpdateSpecFromVersionOneOf(str, Enum):
    """PluginUpdateSpecFromVersionOneOf."""

    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)