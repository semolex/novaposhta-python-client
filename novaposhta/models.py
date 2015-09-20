# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen
from itertools import islice
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
        self.query['apiKey'] = API_SETTINGS['api_key']
        self.query['methodProperties'] = {}
        if API_SETTINGS['api_point']:
            self.api_point = API_SETTINGS['api_point']
        else:    
            self.api_point = 'https://api.novaposhta.ua/v2.0/json/'

    def send(self, data, limit=0):
        """
        Primary method for API requests and data fetching.
        It uses `urllib2` and `json` libs for requests to API through `HTTP` protocol.

        :param data:
            jsonified dict with requests params, based on `self.query` (by default).
        :type data:
            dict
        :param limit:
            integer value, can be used for limiting data amount from response.
            Data will be limited for first `n` elements (where `n` = limit value).
            Also, response metadata(response['info'] etc.) will be flushed (only `response['data']` will be returned).
        :type limit
            int
        :return:
            dictionary or list with fetched data
         :rtype:
            dict or list
        """
        req = Request(self.api_point, json.dumps(data))
        response = json.load(urlopen(req))
        if limit:
            response = list(islice(response['data'], limit))
        return response

    def method(self, method):
        self.query['calledMethod'] = method

    def method_props(self, props):
        self.query['methodProperties'] = props


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
            self.get_city_ref(city='Zdolbuniv')
        :param city:
            name of the required city
        :type city:
            str or unicode
        :return:
            parsed `CityRef` value (hash)
        :rtype:
            unicode
        """
        city_ref = self.get_city_by_name(city=city)['data'][0]['Ref']
        return city_ref

    def get_cities(self, limit=0):
        """
        Method for parsing all cities data.
        API method: `getCities`.

        :Usage:
            self.get_cities()
        :return:
            parsed dictionary of all cities data
        :rtype:
            dict
        """
        self.method('getCities')
        self.method_props({})
        req = self.send(self.query, limit=limit)
        return req

    def get_city_by_name(self, city):
        """
        Method for parsing city data by city name.
        API method: `getCities`.
        API method properties: `FindByString`.

        :param city:
            str or unicode
        :return:
            parsed dictionary with city data
        :rtype:
            dict
        """
        self.method('getCities')
        self.method_props({"FindByString": city})
        req = self.send(self.query)
        return req

    def get_streets(self, city):
        """
        Method for parsing all streets data at provided city.
        API method: `getStreet`.
        API method properties: `CityRef`.

        Usage:
            self.get_streets(city='Zdolbuniv')
        :param city:
            str or unicode
        :return:
            parsed dictionary with streets data
         :rtype:
            dict
        """
        city_ref = self.get_city_ref(city=city)
        self.method('getStreet')
        self.method_props({"CityRef": city_ref})
        req = self.send(self.query)
        return req

    def get_street_by_name(self, city, street):
        """
        Method for parsing specific street data at provided city.
        API method: `getStreet`.
        API method properties: `FindByString`, `CityRef`.

        :Usage:
            self.get_street_by_name(city='Zdolbuniv', street='Nezalezhnosti`)
        :param city:
            str or unicode
        :param street:
            str or unicode
        :return:
            parsed dictionary with street data
         :rtype:
            dict
        """
        city_ref = self.get_city_ref(city=city)
        self.method('getStreet')
        self.method_props({"CityRef": city_ref, "FindByString": street})
        req = self.send(self.query)
        return req

    def get_warehouses(self, city):
        """
        Method for parsing all warehouses data at provided city.
        API method: `getWarehouses`.
        API method properties: `CityRef`.

        :Usage:
            self.get_warehouses(city='Zdolbuniv')
        :param city:
            str or unicode
        :return:
            parsed dictionary with all warehouses data
         :rtype:
            dict
        """
        city_ref = self.get_city_ref(city=city)
        self.method('getWarehouses')
        self.method_props({"CityRef": city_ref})
        req = self.send(self.query)
        return req

    def get_warehouse_types(self):
        """
        Method for parsing warehouse types data .
        API method: `getWarehouseTypes`.

        :Usage:
            self.get_warehouse_types()
        :return:
            parsed dictionary with warehouse types data
        :rtype:
            dict
        """
        self.method('getWarehouseTypes')
        req = self.send(self.query)
        return req

    def get_areas(self, limit=0):
        """
        Method for parsing geographical areas data.
        API method: `getAreas`.

        :Usage:
            self.get_areas()
        :return:
            parsed dictionary with areas data
        :rtype:
            dict
        """
        self.method('getAreas')
        self.method_props({})
        req = self.send(self.query, limit=limit)
        return req


class Counterparty(NovaPoshtaApi):

        def get_counterparties(self, cp_type='Sender'):
            self.method('getCounterparties')
            self.method_props({"CounterpartyProperty": cp_type})
            req = self.send(self.query)
            return req

        def get_counterparty_by_name(self, name, cp_type='Sender'):
            self.method('getCounterparties')
            self.method_props({"CounterpartyProperty": cp_type, 'FindByString': name})
            req = self.send(self.query)
            return req

        def get_counterparty_ref(self, name, cp_type='Sender'):
            self.method('getCounterparties')
            self.method_props({"CounterpartyProperty": cp_type, 'FindByString': name})
            req = self.send(self.query)['data'][0]['Ref']
            return req

        def get_counterparty_by_ERDPOU(self, city, code):
            city_ref = Address().get_city_by_name(city)['data'][0]['Ref']
            self.method('getCounterpartyByEDRPOU')
            self.method_props({"CityRef": city_ref, 'EDRPOU': code})
            req = self.send(self.query)
            return req

        def ex_get_counterparty_by_ERDPOU(self, city_ref, code):
            self.method('getCounterpartyByEDRPOU')
            self.method_props({"CityRef": city_ref, 'EDRPOU': code})
            req = self.send(self.query)
            return req

        def get_counterparty_addresses(self, name, cp_type='Sender'):
            cp_ref = self.get_counterparty_ref(name=name, cp_type=cp_type)
            self.method('getCounterpartyAddresses')
            self.method_props({'Ref': cp_ref, 'CounterpartyProperty': cp_type})
            req = self.send(self.query)
            return req

        def ex_get_counterparty_addresses(self, cp_ref, cp_type='Sender'):
            self.method('getCounterpartyAddresses')
            self.method_props({'Ref': cp_ref, 'CounterpartyProperty': cp_type})
            req = self.send(self.query)
            return req

        def get_counterparty_contact_persons(self, name, cp_type):
            cp_ref = self.get_counterparty_ref(name=name, cp_type=cp_type)
            self.method('getCounterpartyContactPersons')
            self.method_props({'Ref': cp_ref})
            return self.send(self.query)

        def ex_get_counterparty_contact_persons(self, cp_ref):
            self.method('getCounterpartyContactPersons')
            self.method_props({'Ref': cp_ref})
            return self.send(self.query)

