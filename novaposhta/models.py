# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen
import json

API_SETTINGS = {'api_key': '', 'api_point': ''}


class NovaPoshtaApi(object):
    """A base API class, that holds shared methods and settings for other models.
    Creates basic query object and provide `apiKey` and API endpoint configuration.
    """

    def __init__(self):
        """
        Creates basic configuration dictionary, used as API query template by models.
        Settings can be set through `API_SETTINGS` variable.
        """
        self.query = {} or dict()
        self.query['modelName'] = self.__class__.__name__
        self.query['methodProperties'] = {}
        self.query['apiKey'] = API_SETTINGS['api_key']
        if API_SETTINGS['api_point']:
            self.api_point = API_SETTINGS['api_point']
        else:
            self.api_point = 'https://api.novaposhta.ua/v2.0/json/'

    def send(self, method=None, method_props=None):
        """
        Primary method for API requests and data fetching.
        It uses `urllib2` and `json` libs for requests to API through `HTTP` protocol.
        Modifies API template and then makes request to API endpoint.

        :param method (string or unicode):
            name of the API method, should be passed for every request
        :param method_props (dict (key: str, value: str)):
            additional params for API methods.
        :return:
             dict: dictionary with fetched data
        """
        self.query['calledMethod'] = method
        if method_props:
            self.query['methodProperties'] = method_props
        req = Request(self.api_point, json.dumps(self.query))
        response = json.load(urlopen(req))
        return response


class Address(NovaPoshtaApi):
    """A class representing the Address model of Nova Poshta API.
    Uses API methods for parsing, like `getCities`, `getStreet` etc.
    Used for parsing `geo` data like cities, streets etc.
    """

    def get_city_ref(self, city):
        """
        Method for parsing `CityRef` data (unique city hash) from API, required for other methods.
        Uses `get_city_by_name` method.
        API method: `getCities`.

        :Usage:
         address = Address()
         address.get_city_ref(city=u'Здолбунів')
        :param city (str or unicode):
            name of the required city
        :return:
            unicode: parsed `CityRef` value (hash)
        """
        city_ref = self.get_city_by_name(city=city)['data'][0]['Ref']
        return city_ref

    def get_cities(self):
        """
        Method for parsing all cities data.
        API method: `getCities`.

        :Usage:
            address = Address()
            address.get_cities()
        :return:
            dict: parsed dictionary of all cities data
        """
        req = self.send(method='getCities')
        return req

    def get_city_by_name(self, city):
        """
        Method for parsing city data by city name.
        API method: `getCities`.
        API method properties: `FindByString`.

        :Usage:
            address = Address()
            address.get_city_by_name(city=u'Здолбунів')
        :param city (str or unicode):
            name of the desired city
        :return:
            dict: parsed dictionary with city data
        """
        req = self.send(method='getCities', method_props={'FindByString': city})
        return req

    def ex_get_streets(self, city):
        """
        Method for parsing all streets data at provided city.
        API method: `getStreet`.
        API method properties: `CityRef`.

        :Usage:
            address = Address()
            address.get_streets(city=u'Здолбунів')
        :param city (str or unicode):
            name of the desired city
        :return:
            dict: parsed dictionary with streets data
        """
        city_ref = self.get_city_ref(city=city)
        req = self.send(method='getStreet', method_props={"CityRef": city_ref})
        return req

    def get_streets(self, city_ref):
        """
        Method for parsing all streets data at provided city.
        API method: `getStreet`.
        API method properties: `CityRef`.

        Usage:
            address = Address()
            address.get_streets(city_ref='0006560c-4079-11de-b509-001d92f78698')
        :param city_ref (str or unicode):
            string with ID of the target city
        :return:
            dict: parsed dictionary with streets data
        """
        req = self.send(method='getStreet', method_props={"CityRef": city_ref})
        return req

    def ex_get_street_by_name(self, city, street):
        """
        Method for parsing specific street data at provided city.
        API method: `getStreet`.
        API method properties: `FindByString`, `CityRef`.

        :Usage:
            address = Address()
            address.ex_get_street_by_name(city=u'Здолбунів', street=u'Незалежності')
        :param city (str or unicode):
            string with the name of the target city
        :param street (str or unicode):
            string with the name of the target street
        :return:
            dict: parsed dictionary with street data
        """
        city_ref = self.get_city_ref(city=city)
        req = self.send(method='getStreet', method_props={'CityRef': city_ref, 'FindByString': street})
        return req

    def get_street_by_name(self, city_ref, street):
        """
        Method for parsing specific street data at provided city.
        API method: `getStreet`.
        API method properties: `FindByString`, `CityRef`.

        :Usage:
            address = Address()
            address.get_street_by_name(city_ref='0006560c-4079-11de-b509-001d92f78698', street=u'Незалежності')
        :param city_ref (str or unicode):
            string with ID of the target city
        :param street (str or unicode):
            string with the name of the target street
        :return:
            dict: parsed dictionary with street data
        """
        req = self.send(method='getStreet', method_props={"CityRef": city_ref, "FindByString": street})
        return req

    def ex_get_warehouses(self, city):
        """
        Method for parsing all warehouses data at provided city.
        API method: `getWarehouses`.
        API method properties: `CityRef`.

        :Usage:
            address = Address()
            address.get_warehouses(city=u'Здолбунів')
        :param city (str or unicode):
            string with the name of the target city
        :return:
            dict: parsed dictionary with all warehouses data
        """
        city_ref = self.get_city_ref(city=city)
        req = self.send(method='getWarehouses', method_props={'CityRef': city_ref})
        return req

    def get_warehouses(self, city_ref):
        """
        Method for parsing all warehouses data at provided city.
        API method: `getWarehouses`.
        API method properties: `CityRef`.

        :Usage:
            address = Address()
            address.get_warehouses(city='0006560c-4079-11de-b509-001d92f78698')
        :param city_ref:
            string with ID of the target city
        :return:
            dict: parsed dictionary with all warehouses data
        """
        req = self.send(method='getWarehouses', method_props={"CityRef": city_ref})
        return req

    def get_warehouse_types(self):
        """
        Method for parsing warehouse types data .
        API method: `getWarehouseTypes`.

        :Usage:
            address = Address()
            address.get_warehouse_types()
        :return:
            dict: parsed dictionary with warehouse types data
        """
        req = self.send(method='getWarehouseTypes')
        return req

    def get_areas(self):
        """
        Method for parsing geographical areas data.
        API method: `getAreas`.

        :Usage:
            address = Address()
            address.get_areas()
        :return:
            dict: parsed dictionary with areas data
        """
        req = self.send(method='getAreas')
        return req


class Counterparty(NovaPoshtaApi):
    def get_counterparties(self, cp_type='Sender'):
        req = self.send(method='getCounterparties', method_props={"CounterpartyProperty": cp_type})
        return req

    def get_counterparty_by_name(self, name, cp_type='Sender'):
        req = self.send(method='getCounterparties',
                        method_props={"CounterpartyProperty": cp_type, 'FindByString': name})
        return req

    def get_counterparty_ref(self, name, cp_type='Sender'):
        props = {'CounterpartyProperty': cp_type, 'FindByString': name}  # separate for a better look :)
        req = self.send(method='getCounterparties', method_props=props)
        return req

    def ex_get_counterparty_by_ERDPOU(self, city, code):
        city_ref = Address().get_city_by_name(city)['data'][0]['Ref']
        req = self.send(method='getCounterpartyByEDRPOU', method_props={"CityRef": city_ref, 'EDRPOU': code})
        return req

    def get_counterparty_by_ERDPOU(self, city_ref, code):
        req = self.send(method='getCounterpartyByEDRPOU', method_props={"CityRef": city_ref, 'EDRPOU': code})
        return req

    def ex_get_counterparty_addresses(self, name, cp_type='Sender'):
        cp_ref = self.get_counterparty_ref(name=name, cp_type=cp_type)
        req = self.send(method='getCounterpartyAddresses',
                        method_props={'Ref': cp_ref, 'CounterpartyProperty': cp_type})
        return req

    def get_counterparty_addresses(self, cp_ref, cp_type='Sender'):
        req = self.send(method='getCounterpartyAddresses',
                        method_props={'Ref': cp_ref, 'CounterpartyProperty': cp_type})
        return req

    def ex_get_counterparty_contact_persons(self, name, cp_type):
        cp_ref = self.get_counterparty_ref(name=name, cp_type=cp_type)
        req = self.send(method='getCounterpartyContactPersons', method_props={'Ref': cp_ref})
        return req

    def get_counterparty_contact_persons(self, cp_ref):
        req = self.send(method='getCounterpartyContactPersons', method_props={'Ref': cp_ref})
        return req


class Common(NovaPoshtaApi):
    def get_payment_forms(self):
        req = self.send(method='getPaymentForms')
        return req

    def get_cargo_types(self):
        req = self.send(method='getCargoTypes')
        return req

    def get_service_types(self):
        req = self.send(method='getServiceTypes')
        return req

    def get_cargo_description_list(self):
        req = self.send(method='getCargoDescriptionList')
        return req

    def search_cargo_description_list(self, keyword):
        req = self.send(method='getCargoDescriptionList', method_props={'FindByString': keyword})
        return req

    def get_ownership_forms_list(self):
        req = self.send(method='getOwnershipFormsList')
        return req

    def get_backward_delivery_cargo_types(self):
        req = self.send('getBackwardDeliveryCargoTypes')
        return req

    def get_pallets_list(self):
        req = self.send(method='getPalletsList')
        return req

    def get_type_of_counterparties(self):
        req = self.send(method='getTypesOfCounterparties')
        return req

    def get_type_of_payers_for_redelivery(self):
        req = self.send(method='getTypesOfPayersForRedelivery')
        return req

    def ex_get_time_intervals(self, city, datetime):
        city_ref = Address().get_city_by_name(city)['data'][0]['Ref']
        req = self.send(method='getTimeIntervals', method_props={'RecipientCityRef': city_ref, 'DateTime': datetime})
        return req

    def get_time_intervals(self, city_ref, datetime):
        req = self.send(method='getTimeIntervals', method_props={'RecipientCityRef': city_ref, 'DateTime': datetime})
        return req

    def get_tires_wheels_list(self):
        req = self.send(method='getTiresWheelsList')
        return req

    def get_trays_list(self):
        req = self.send(method='getTraysList')
        return req

    def get_document_statuses(self):
        req = self.send(method='getDocumentStatuses')
        return req

    def get_document_state(self, state_id):
        req = self.send(method='getDocumentStatuses', method_props={'StateId': state_id})
        return req
