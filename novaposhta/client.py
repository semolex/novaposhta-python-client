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
from .types import DictStrAny

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
    ):
        """
        Initialize Nova Poshta API client.

        :param api_key: API key from Nova Poshta.
        :param api_endpoint: API endpoint to use.
        :param http_client: HTTP client to use. Defaults to httpx.
        :param timeout: Timeout for HTTP requests.
        """
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.http_client = http_client.Client
        self.timeout = timeout
        self._models_pool = {}

    def send(
        self, model_name: str, api_method: str, method_props: DictStrAny
    ) -> DictStrAny:
        """
        Sends request to the API.

        :param model_name: name of the model to use.
        :param api_method: name of the method to call.
        :param method_props: properties to pass to the method.
        :return: response dict.
        """
        request = {
            "apiKey": self.api_key,
            "modelName": model_name,
            "calledMethod": api_method,
            "methodProperties": method_props,
        }
        with self.http_client() as client:
            response = client.post(
                self.api_endpoint, json=request, headers=HEADERS, timeout=self.timeout
            )
        return response.json()

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
