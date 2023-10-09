"""Python client for Nova Poshta company's API. """

import httpx

from novaposhta.models.base import BaseModel
from novaposhta.models.address import Address
from novaposhta.models.counterparty import Counterparty
from novaposhta.models.contact_person import ContactPerson
from novaposhta.models.scan_sheet import ScanSheet
from novaposhta.models.common import Common
from novaposhta.models.additional_service import AdditionalService
from novaposhta.models.internet_document import InternetDocument
from novaposhta.models.tracking_document import TrackingDocument

from typing import Type

HEADERS = {"Content-Type": "application/json"}


class NovaPoshtaApi:
    """
    Base class that wraps call to the Nova Poshta API.
    Prepares requests and builds proper resource location.
    All API models can be accessed as instance properties.
    Info about models can be found here:
    https://devcenter.novaposhta.ua/docs/services/
    """

    def __init__(
        self,
        api_key,
        api_endpoint="https://api.novaposhta.ua/v2.0/json/",
        http_client=httpx,
        timeout=10,
    ):
        """
        :param api_key: API key from Nova Poshta.
        :param api_endpoint: API endpoint to use.
        :param http_client: HTTP client to use. Defaults to httpx.
        :param timeout: Timeout for HTTP requests.
        """
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.http_client = http_client
        self.timeout = timeout
        self._models_pool = {}

    def send(self, model_name, api_method, method_props):
        request = {
            "apiKey": self.api_key,
            "modelName": model_name,
            "calledMethod": api_method,
            "methodProperties": method_props,
        }
        print(request)
        response = self.http_client.post(
            self.api_endpoint, json=request, headers=HEADERS, timeout=self.timeout
        )
        return response.json()

    def new(self, model: Type[BaseModel]):
        """
        Explicitly add/reset new model to the pool.
        :param model: model to add.
        """
        if model.name in self._models_pool:
            del self._models_pool[model.name]
        self._models_pool[model.name] = model(self)
        return self._models_pool[model.name]

    @property
    def address(self) -> Type[Address]:
        """
        Gives access to the Address model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7ccaa0fe4f08e8f7ce43
        """
        return self.new(Address)

    @property
    def counterparty(self) -> Type[Counterparty]:
        """
        Gives access to the Counterparty model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c8ea0fe4f08e8f7ce42
        """
        return self.new(Counterparty)

    @property
    def contact_person(self) -> Type[ContactPerson]:
        """
        Gives access to the ContactPerson model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c7da0fe4f08e8f7ce41
        """
        return self.new(ContactPerson)

    @property
    def scan_sheet(self) -> Type[ScanSheet]:
        """
        Gives access to the ScanSheet model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c7da0fe4f08e8f7ce41
        """
        return self.new(ScanSheet)

    @property
    def common(self) -> Type[Common]:
        """
        Gives access to the Common model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c7da0fe4f08e8f7ce41
        """
        return self.new(Common)

    @property
    def additional_service(self) -> Type[AdditionalService]:
        """
        Gives access to the AdditionalService model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c7da0fe4f08e8f7ce41
        """
        return self.new(AdditionalService)

    @property
    def internet_document(self) -> Type[InternetDocument]:
        """
        Gives access to the InternetDocument model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c7da0fe4f08e8f7ce41
        """
        return self.new(InternetDocument)

    @property
    def tracking_document(self) -> Type[TrackingDocument]:
        """
        Gives access to the TrackingDocument model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7c7da0fe4f08e8f7ce41
        """
        return self.new(TrackingDocument)
