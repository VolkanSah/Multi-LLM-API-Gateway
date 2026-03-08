# app/models.py
from . import config
import logging

logger = logging.getLogger("models")

_registry: dict = {}

def initialize() -> None:
    """Build model registry from .pyfun [MODELS]"""
    global _registry
    _registry = config.get_models()
    logger.info(f"Models loaded: {list(_registry.keys())}")


def get(model_name: str) -> dict:
    """Get model config by name."""
    return _registry.get(model_name, {})


def get_limit(model_name: str, key: str, default=None):
    """Get specific limit for a model."""
    return _registry.get(model_name, {}).get(key, default)


def for_provider(provider_name: str) -> dict:
    """Get all models for a provider."""
    return config.get_models_for_provider(provider_name)


def max_tokens(model_name: str) -> int:
    return int(get_limit(model_name, "max_output_tokens", "1024"))


def context_size(model_name: str) -> int:
    return int(get_limit(model_name, "context_tokens", "4096"))


def cost_input(model_name: str) -> float:
    return float(get_limit(model_name, "cost_input_per_1k", "0"))


def cost_output(model_name: str) -> float:
    return float(get_limit(model_name, "cost_output_per_1k", "0"))


def list_all() -> list:
    return list(_registry.keys())
