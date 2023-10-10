"""BaseModel module."""

from functools import wraps
from typing import Any

from ..types import DictStrAny


def api_method(method_name: str):
    """
    Decorator for methods to provide the api method name.
    :param method_name: name of the method from API.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            props = func(self, *args, **kwargs)
            return self._call(method_name, props)

        return wrapper

    return decorator


class BaseModel:
    """
    Base model class for all models.
    """

    name = "base"

    def __init__(self, client):
        self._client = client

    def _call(self, method: str, props: DictStrAny):
        """
        Wraps call to the API by using client. Automatically passes model name.

        :param method: name of the called method from API.
        :param props: payload to send to API.
        :return: response dict.
        """
        return self._client.send(self.name, method, props)

    @staticmethod
    def _call_with_props(**properties: Any):
        """
        Filters out empty properties, convert to string and returns only those that have values.

        :param properties: properties to filter.
        :return: filtered properties.
        """
        props = {
            k: str(v) if not isinstance(v, (list, dict)) else v
            for k, v in properties.items()
            if v is not None
        }
        return props

    def __str__(self):
        """
        String representation of the model.
        """
        return self.name
