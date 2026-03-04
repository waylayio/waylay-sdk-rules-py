"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.bayesian_graph import BayesianGraph
from ..models.simplified_graph import SimplifiedGraph

GraphDefinition: TypeAlias = SimplifiedGraph | BayesianGraph
"""GraphDefinition."""
