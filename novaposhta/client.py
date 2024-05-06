"""Client for Nova Poshta API. """

from typing import Type, TypeVar, Optional, Callable

import httpx

from .models.additional_service import AdditionalService
from .models.address import Address
from .models.base import BaseModel
from .models.common import Common
from .models.contact_person import ContactPerson
from .models.counterparty import Counterparty
from .models.internet_document import InternetDocument
from .models.scan_sheet import ScanSheet
from .models.tracking_document import TrackingDocument
from .types import DictStrAny, MaybeAsync

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

    sync_http_client: Optional[httpx.Client] = None
    async_http_client: Optional[httpx.AsyncClient] = None

    def __init__(
        self,
        api_key: str,
        api_endpoint: str = "https://api.novaposhta.ua/v2.0/json/",
        http_client=httpx,
        timeout: int = 10,
        raise_for_errors: bool = False,
        async_mode: bool = False,
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
        self.timeout = timeout
        self._send: Callable[[DictStrAny], MaybeAsync]
        if async_mode:
            self.async_http_client: Optional[httpx.AsyncClient] = (
                http_client.AsyncClient(timeout=timeout)
            )
            self._send = self._send_async
        else:
            self.sync_http_client: Optional[httpx.Client] = http_client.Client(
                timeout=timeout
            )
            self._send = self._send_sync
        self.raise_for_errors = raise_for_errors
        self.async_mode = async_mode
        self._models_pool: DictStrAny = {}

    def _send_sync(self, request: DictStrAny) -> DictStrAny:
        """
        Sends sync request to the API.

        :param request: request dict.
        :return: response dict.
        """
        if not self.sync_http_client:
            raise ValueError("Sync client is not initialized")
        response = self.sync_http_client.post(**request)
        return self._maybe_check_errors(response.json())

    async def _send_async(self, request: DictStrAny) -> DictStrAny:
        """
        Sends async request to the API.

        :param request: request dict.
        :return: response dict.
        """
        if not self.async_http_client:
            raise ValueError("Async client is not initialized")
        response: httpx.Response = await self.async_http_client.post(**request)
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

    def get(self, name: str) -> Optional[BaseModel]:
        """
        Get model from the pool.

        :param name: name of the model to get.
        """
        return self._models_pool.get(name)

    def _maybe_check_errors(self, response: DictStrAny) -> DictStrAny:
        """
        Check response for errors.

        :param response: response dict.
        :return: response dict.
        """
        if not self.raise_for_errors:
            return response

        if response["success"]:
            return response

        error = response["errors"][0]
        if error.startswith("API key"):
            raise InvalidAPIKeyError(error)
        else:
            raise APIRequestError(error)

    def close_sync(self):
        """
        Close sync client.
        """
        if self.sync_http_client:
            self.sync_http_client.close()

    async def close_async(self):
        """
        Close async client.
        """
        if self.async_http_client:
            await self.async_http_client.aclose()

    def __enter__(self):
        """
        Enter the context.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context.
        Close the client.
        """
        self.close_sync()

    async def __aenter__(self):
        """
        Enter the async context.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the async context.
        """
        await self.close_async()

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
