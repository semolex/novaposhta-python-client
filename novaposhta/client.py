"""Client for Nova Poshta API. """

import httpx

from .models.base import BaseModel
from .models.address import Address
from .models.counterparty import Counterparty
from .models.contact_person import ContactPerson
from .models.scan_sheet import ScanSheet
from .models.common import Common
from .models.additional_service import AdditionalService
from .models.internet_document import InternetDocument
from .models.tracking_document import TrackingDocument
from .types import DictStrAny, MaybeAsync

from typing import Type, TypeVar, Union

HEADERS = {"Content-Type": "application/json"}

BaseModelType = TypeVar("BaseModelType", bound=BaseModel)


class NovaPoshtaApi:
    """
    Base class that wraps call to the Nova Poshta API.
    Prepares requests and builds proper resource location.
    All API models can be accessed as instance properties.
    Info about models can be found here:
    https://developers.novaposhta.ua/documentation
    """

    def __init__(
        self,
        api_key,
        api_endpoint="https://api.novaposhta.ua/v2.0/json/",
        http_client=httpx,
        timeout=10,
        raise_for_errors=False,
        async_mode=False,
    ):
        """
        Initialize Nova Poshta API client.

        :param api_key: API key from Nova Poshta.
        :param api_endpoint: API endpoint to use.
        :param http_client: HTTP client to use. Defaults to httpx.
        :param timeout: Timeout for HTTP requests.
        :param raise_for_errors: Whether to check and raise errors as exceptions.
        :param async_mode: Whether to use async mode.
        """
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.http_client = (
            http_client.Client if not async_mode else http_client.AsyncClient
        )
        self.timeout = timeout
        self.raise_for_errors = raise_for_errors
        self.async_mode = async_mode
        self._models_pool = {}

        if self.async_mode:
            self._send = self._send_async

        else:
            self._send = self._send_sync

    def _send_sync(self, request: DictStrAny) -> DictStrAny:
        """
        Sends sync request to the API.

        :param request: request dict.
        :return: response dict.
        """

        with self.http_client() as client:
            response = client.post(**request)
        return self._maybe_check_errors(response.json())

    async def _send_async(self, request: DictStrAny) -> DictStrAny:
        """
        Sends async request to the API.

        :param request: request dict.
        :return: response dict.
        """
        async with self.http_client() as client:
            response = await client.post(**request)
        return self._maybe_check_errors(response.json())

    def send(
        self, model_name: str, api_method: str, method_props: DictStrAny
    ) -> MaybeAsync:
        """
        Sends request to the API.

        :param model_name: name of the model to use.
        :param api_method: name of the method to call.
        :param method_props: properties to pass to the method.
        :return: response dict.
        """
        data = {
            "apiKey": self.api_key,
            "modelName": model_name,
            "calledMethod": api_method,
            "methodProperties": method_props,
        }
        request = {
            "url": self.api_endpoint,
            "headers": HEADERS,
            "json": data,
            "timeout": self.timeout,
        }
        return self._send(request)

    def new(self, model: Type[BaseModelType]) -> BaseModelType:
        """
        Provide access to the given model of Nova Poshta API.

        This property initializes a new model and provides
        access to its methods and attributes, facilitating interactions
        with the Nova Poshta API for model-related operations.

        :param model: model to add.
        """
        if model.name in self._models_pool:
            del self._models_pool[model.name]
        self._models_pool[model.name] = model(self)
        return self._models_pool[model.name]

    def get(self, name: str) -> Union[BaseModelType, None]:
        """
        Get model from the pool.

        :param name: name of the model to get.
        """
        return self._models_pool.get(name)

    def _maybe_check_errors(self, response):
        if not self.raise_for_errors:
            return response

        if response["success"]:
            return response

        error = response["errors"][0]
        if error.startswith("API key"):
            raise InvalidAPIKeyError(error)
        else:
            raise APIRequestError(error)

    @property
    def address(self) -> Address:
        """
        Provide access to the Address model.
        """
        return self.new(Address)

    @property
    def counterparty(self) -> Counterparty:
        """
        Provide access to the Counterparty model.
        """
        return self.new(Counterparty)

    @property
    def contact_person(self) -> ContactPerson:
        """
        Provide access to the ContactPerson model.
        """
        return self.new(ContactPerson)

    @property
    def scan_sheet(self) -> ScanSheet:
        """
        Provide access to the ScanSheet model.
        """
        return self.new(ScanSheet)

    @property
    def common(self) -> Common:
        """
        Provide access to the Common model.
        """
        return self.new(Common)

    @property
    def additional_service(self) -> AdditionalService:
        """
        Provide access to the AdditionalService model.
        """
        return self.new(AdditionalService)

    @property
    def internet_document(self) -> InternetDocument:
        """
        Provide access to the InternetDocument model.
        """
        return self.new(InternetDocument)

    @property
    def tracking_document(self) -> TrackingDocument:
        """
        Provide access to the TrackingDocument model.
        """
        return self.new(TrackingDocument)


class NovaPoshtaError(Exception):
    """General Nova Poshta exception."""


class InvalidAPIKeyError(NovaPoshtaError):
    """Invalid API key exception."""


class APIRequestError(NovaPoshtaError):
    """Invalid API request exception."""
