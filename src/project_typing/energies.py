"""Enum de Energias"""
from .base_enum import BaseEnum


class EnergiesEnum(BaseEnum):
  """Enum de energias existentes"""
  POSITIVA = "positiva"
  NEGATIVA = "negativa"
  QUALQUER = "qualquer"