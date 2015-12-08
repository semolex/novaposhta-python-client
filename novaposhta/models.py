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
        self.query = {
            'modelName': self.__class__.__name__,
            'methodProperties': {},
            'apiKey': API_SETTINGS['api_key']
        }
        if API_SETTINGS['api_point']:
            self.api_point = API_SETTINGS['api_point']
        else:
            self.api_point = 'https://api.novaposhta.ua/v2.0/json/'

    @staticmethod
    def _clean_properties(method_properties):
        return dict((k, v) for k, v in method_properties.iteritems() if v)

    def send(self, method=None, method_props=None):
        """
        Primary method for API requests and data fetching.
        It uses `urllib2` and `json` libs for requests to API through `HTTP` protocol.
        Modifies API template and then makes request to API endpoint.

        :param method:
            name of the API method, should be passed for every request
        :type method:
            str or unicode
        :param method_props:
            additional params for API methods.
        :type method_props:
            dict
        :return:
            dictionary with fetched info
        :rtype:
            dict
        """
        self.query['calledMethod'] = method
        if method_props:
            self.query['methodProperties'] = self._clean_properties(method_props)
        req = Request(self.api_point, json.dumps(self.query))
        response = json.load(urlopen(req))
        return response


class Address(NovaPoshtaApi):
    """A class representing the `Address` model of Nova Poshta API.
    Used for parsing `geodata` (like cities, streets etc.).
    """

    def get_city_ref(self, city):
        """
        Method for fetching `CityRef` (unique city hash) from API, required for other methods.

        :example:
            ``address = Address()``
            ``address.get_city_ref(city=u'Здолбунів')``
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

    def get_cities(self):
        """
        Method for fetching info about all cities.

        :example:
            ``address = Address()``
            ``address.get_cities()``
        :return:
            dictionary with info about all cities
        :rtype:
            dict
        """
        req = self.send(method='getCities')
        return req

    def get_city_by_name(self, city):
        """
        Method for fetching info about city by city name.

        :example:
            ``address = Address()``
            ``address.get_city_by_name(city=u'Здолбунів')``
        :param city:
            name of the desired city
        :type city:
            str or unicode
        :return:
            dictionary with info about city
        :rtype:
            dict
        """
        req = self.send(method='getCities', method_props={'FindByString': city})
        return req

    def ex_get_streets(self, city):
        """
        Method for fetching all info about streets in provided city.
        Extended version of `get_streets` method.
        City name is used instead of ID.

        :example:
            ``address = Address()``
            ``address.get_streets(city=u'Здолбунів')``
        :param city:
            name of the desired city
        :type city:
            str or unicode
        :return:
            dictionary with info about streets
        :rtype:
            dict
        """
        city_ref = self.get_city_ref(city=city)
        req = self.send(method='getStreet', method_props={"CityRef": city_ref})
        return req

    def get_streets(self, city_ref):
        """
        Method for fetching info about streets in desired city.

        :example:
            ``address = Address()``
            ``address.get_streets(city_ref='0006560c-4079-11de-b509-001d92f78698')``
        :param city_ref:
            ID of the target city
        :type city_ref:
            str or unicode
        :return:
            dictionary with info about streets
        :rtype:
            dict
        """
        req = self.send(method='getStreet', method_props={"CityRef": city_ref})
        return req

    def ex_get_street_by_name(self, city, street):
        """
        Method for fetching info about specific street in desired city.
        Extended version of `get_street_by_name` method.
        City name is used instead of ID.

        :example:
            ``address = Address()``
            ``print address.ex_get_street_by_name(city=u'Здолбунів', street=u'Незалежності')``
        :param city:
            name of the target city
        :type city:
            str or unicode
        :param street:
            name of the street
        :type street:
            str or unicode
        :return:
            dictionary with info about street
        :rtype:
            dict
        """
        city_ref = self.get_city_ref(city=city)
        req = self.send(method='getStreet', method_props={'CityRef': city_ref, 'FindByString': street})
        return req

    def get_street_by_name(self, city_ref, street):
        """
        Method for fetching info about specific street in desired city.

        :example:
            ``address = Address()``
            ``address.get_street_by_name(city_ref='0006560c-4079-11de-b509-001d92f78698', street=u'Незалежності')``
        :param city_ref:
            ID of the target city
        :type city_ref:
            str or unicode
        :param street:
            name of the target street
        :type street:
            str or unicode
        :return:
            dictionary with info about street
        :rtype:
            dict
        """
        req = self.send(method='getStreet', method_props={"CityRef": city_ref, "FindByString": street})
        return req

    def ex_get_warehouses(self, city):
        """
        Method for fetching info about all warehouses in desired city.
        Extended version of `get_warehouses` method.
        City name is used instead of ID.

        :example:
            ``address = Address()``
            ``address.get_warehouses(city=u'Здолбунів')``
        :param city:
            name of the target city
        :type city:
            str or unicode
        :return:
            parsed dictionary with all info about warehouses
        :rtype:
            dict
        """
        city_ref = self.get_city_ref(city=city)
        req = self.send(method='getWarehouses', method_props={'CityRef': city_ref})
        return req

    def get_warehouses(self, city_ref):
        """
        Method for fetching info about all warehouses in desired city.

        :example:
            ``address = Address()``
            ``address.get_warehouses(city='0006560c-4079-11de-b509-001d92f78698')``
        :param city_ref:
            ID of the target city
        :type city_ref:
            str or unicode
        :return:
            parsed dictionary with all info about warehouses
        :rtype:
            dict
        """
        req = self.send(method='getWarehouses', method_props={"CityRef": city_ref})
        return req

    def get_warehouse_types(self):
        """
        Method for fetching info about warehouse's types.

        :example:
            ``address = Address()``
            ``address.get_warehouse_types()``
        :return:
            parsed dictionary with info about warehouse's types
        :rtype:
            dict
        """
        req = self.send(method='getWarehouseTypes')
        return req

    def get_areas(self):
        """
        Method for fetching info about areas geographical areas.

        :example:
            ``address = Address()``
            ``address.get_areas()``
        :return:
            parsed dictionary with info about areas
        :rtype:
            dict
        """
        req = self.send(method='getAreas')
        return req

    def save(self, from_data=None, cp_ref=None, str_ref=None, build_num=None, flat=None, note=None):
        """
        Method for saving counterparty's address

        :example:
            ``address = Address()``
            ``address.save(cp_ref='5953fb16-08d8-11e4-8958-0025909b4e33',``
            ``str_ref='d8364179-4149-11dd-9198-001d60451983', build_num=u'20',``
            ``flat=u'10')``
            or:
            ``address = Address()``
            ``data = {
            ``        cp_ref='5953fb16-08d8-11e4-8958-0025909b4e33',``
            ``        str_ref='d8364179-4149-11dd-9198-001d60451983',
            ``        build_num=u'20',``
            ``        flat=u'10'}``
            ``address.save(from_data=data)``
        :param from_data:
            dictionary with all required data, will be used instead of passing each keyword separately
        :type from_data:
            dict
        :param cp_ref:
            ID of the counterparty
        :type cp_ref:
            str or unicode
        :param str_ref:
            ID of the street
        :type str_ref:
            str or unicode
        :param build_num:
            building number
        :type build_num:
            str or unicode
        :param flat:
            flat number
        :type flat:
            str or unicode
        :param note:
            comment
        :type:
            str or unicode
        :return:
            dictionary with info about saved address
        :rtype:
             dict
        """
        if from_data:
            props = from_data
        else:
            props = {
                'CounterpartyRef': cp_ref,
                'StreetRef': str_ref,
                'BuildingNumber': build_num,
                'Flat': flat,
                'Note': note
            }
        req = self.send(method='save', method_props=props)
        return req

    def update(self, from_data=None, cp_ref=None, add_ref=None, str_ref=None, build_num=None, flat=None, note=None):
        """
        Method for updating counterparty's address

        :param from_data:
            dictionary with all required data, will be used instead of passing each keyword separately
        :type from_data:
            dict
        :param cp_ref:
            ID of the counterparty
        :type cp_ref:
            str or unicode
        :param add_ref:
            ID of the address, that need to be updated
        :type add_ref:
            str or unicode
        :param str_ref:
            ID of the street
        :type str_ref:
            str or unicode
        :param build_num:
            building number
        :type build_num:
            str or unicode
        :param flat:
            flat number
        :type flat:
            str or unicode
        :param note:
            comment
        :type:
            str or unicode
        :return:
            dictionary with info about saved address
        :rtype:
             dict
        """
        if from_data:
            props = from_data
        else:
            props = {
                'CounterpartyRef': cp_ref,
                'Ref': add_ref,
                'StreetRef': str_ref,
                'BuildingNumber': build_num,
                'Flat': flat,
                'Note': note
            }
        req = self.send(method='update', method_props=props)
        return req

    def delete(self, add_ref):
        """
        Method for deleting saved address
        :param add_ref:
            ID of the address, that need to be deleted
        :type add_ref:
            str or unicode
        :return:
            dict with info about deleted address

        """
        props = {
            'Ref': add_ref
        }
        req = self.send(method='delete', method_props=props)
        return req


class Counterparty(NovaPoshtaApi):
    """
    A class representing the `Counterparty` model of Nova Poshta API.
    Used for interact with counterpart's info.
    """

    def get_counterparties(self, cp_type='Sender'):
        """
        Method for fetching all information about counterparties.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparties(cp_type='Recipient')``
        :param cp_type:
            type of the counterparty: can be either `Sender` or `Recipient` (`Sender` used as default)
        :type cp_type:
            str or unicode
        :return:
            dictionary with info about counterparties
        :rtype:
            dict
        """
        req = self.send(method='getCounterparties', method_props={"CounterpartyProperty": cp_type})
        return req

    def get_counterparty_by_name(self, name, cp_type='Sender'):
        """
        Method for fetching info about counterparty by name.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparties(name=u'Талісман', cp_type='Recipient')``
        :param name:
            name of the desired counterparty
        :type name:
            str or unicode
        :param cp_type:
            type of the counterparty: can be either `Sender` or `Recipient` (`Sender` used as default)
        :type cp_type:
            str or unicode
        :return:
            dictionary with info about counterparty
        :rtype:
            dict
        """
        req = self.send(method='getCounterparties',
                        method_props={"CounterpartyProperty": cp_type, 'FindByString': name})
        return req

    def get_counterparty_ref(self, name, cp_type='Sender'):
        """
        Method for fetching `Ref` (unique counterparty hash) from API, required for other methods.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparty_ref(name=u'Талісман', cp_type='Recipient')``
        :param name:
            name of the desired counterparty
        :type name:
            str or unicode
        :param cp_type:
            type of the counterparty: can be either `Sender` or `Recipient` (`Sender` used as default)
        :type cp_type:
            str or unicode
        :return:
            ID of the counterparty
        :rtype:
            unicode
        """
        props = {'CounterpartyProperty': cp_type, 'FindByString': name}  # separate for a better look :)
        req = self.send(method='getCounterparties', method_props=props)['data'][0]['Ref']
        return req

    def ex_get_counterparty_by_edrpou(self, city, code):
        """
        Method for fetching info about counterparty by `EDRPOU` - National State Registry
        of Ukrainian Enterprises and Organizations (8-digit code).
        Extended version of `get_counterparty_by_edrpou` method.
        City name is used instead of ID.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.ex_get_counterparty_by_edrpou(city=u'Здолбунів', code='12345678')``
        :param city:
            name of the city of counterparty
        :type city:
            str or unicode
        :param code:
            EDRPOU code of the counterparty
        :type code:
            str or unicode
        :return:
            dictionary with info about counterparty
        :rtype:
            dict
        """
        city_ref = Address().get_city_by_name(city)['data'][0]['Ref']
        req = self.send(method='getCounterpartyByEDRPOU', method_props={"CityRef": city_ref, 'EDRPOU': code})
        return req

    def get_counterparty_by_edrpou(self, city_ref, code):
        """
        Method for fetching info about counterparty by `EDRPOU` - National State Registry
        of Ukrainian Enterprises and Organizations (8-digit code).

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparty_by_edrpou(city_ref=u'0006560c-4079-11de-b509-001d92f78698', code='12345678')``
        :param city_ref:
            ID of the city of counterparty
        :type city_ref:
            str or unicode
        :param code:
            EDRPOU code of the counterparty
        :type code:
            str or unicode
        :return:
            dictionary with info about counterparty
        :rtype:
            dict
        """
        req = self.send(method='getCounterpartyByEDRPOU', method_props={"CityRef": city_ref, 'EDRPOU': code})
        return req

    def ex_get_counterparty_addresses(self, name, cp_type='Sender'):
        """
        Method for fetching counterparty's addresses.
        Extended version of `get_counterparty_addresses` method.
        Counterparty's name is used instead of ID.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.ex_get_counterparty_addresses(u'Талісман', cp_type='Recipient')``
        :param name:
            name of the counterparty
        :type name:
            str or unicode
        :param cp_type:
            type of the counterparty: can be either `Sender` or `Recipient` (`Sender` used as default)
        :type cp_type:
            str or unicode
        :return:
            dictionary with info about counterparty's addresses
        """
        cp_ref = self.get_counterparty_ref(name=name, cp_type=cp_type)
        req = self.send(method='getCounterpartyAddresses',
                        method_props={'Ref': cp_ref, 'CounterpartyProperty': cp_type})
        return req

    def get_counterparty_addresses(self, cp_ref, cp_type='Sender'):
        """
        Method for fetching counterparty's addresses.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparty_addresses(u'f70f1bee-55fd-11e5-8d8d-005056887b8d', cp_type='Recipient')``
        :param cp_ref:
            ID of the counterparty
        :type cp_ref:
            str or unicode
        :param cp_type:
            type of the counterparty: can be either `Sender` or `Recipient` (`Sender` used as default)
        :type cp_type:
            str or unicode
        :return:
            dictionary with info about counterparty's addresses
        """
        req = self.send(method='getCounterpartyAddresses',
                        method_props={'Ref': cp_ref, 'CounterpartyProperty': cp_type})
        return req

    def ex_get_counterparty_contact_persons(self, name, cp_type='Sender'):
        """
        Method for fetching info about counterparty's contact persons.
        Extended version of `get_counterparty_contact_persons` method.
        Counterparty's name is used instead of ID (additionally, counterparty type should be used).

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.ex_get_counterparty_contact_persons(u'Талісман', cp_type='Recipient')``
        :param name:
            name of the counterparty
        :type name:
            str or unicode
        :param cp_type:
            type of the counterparty: can be either `Sender` or `Recipient` (`Sender` used as default)
        :type cp_type:
            str or unicode
        :return:
            dictionary with info about counterparty's contact persons
        """
        cp_ref = self.get_counterparty_ref(name=name, cp_type=cp_type)
        req = self.send(method='getCounterpartyContactPersons', method_props={'Ref': cp_ref})
        return req

    def get_counterparty_contact_persons(self, cp_ref):
        """
        Method for fetching info about counterparty's contact persons.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparty_contact_persons(u'f70f1bee-55fd-11e5-8d8d-005056887b8d')``
        :param cp_ref:
            name of the counterparty
        :type cp_ref:
            str or unicode
        :return:
            dictionary with info about counterparty's contact persons
        """
        req = self.send(method='getCounterpartyContactPersons', method_props={'Ref': cp_ref})
        return req

    def save(self,  # TODO: Default values!
             from_data=None,
             city_ref=None,
             first_name=None,
             mid_name=None,
             last_name=None,
             phone=None, email=None,
             cp_type=None,
             cp_prop=None):
        """
        Method for saving counterparty.
        Named arguments can be used or it is possible to save pre-parsed dictionary with counterparty info.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.save(city_ref='db5c88d7-391c-11dd-90d9-001a92567626', first_name=u'Фелікс',``
            ``mid_name=u'Едуардович', last_name=u'Ковальчук', phone='0937979489',``
            ``email='myemail@my.com', cp_type='PrivatePerson', cp_prop='Recipient')``
            or:
            ``counterparty = Counterparty()``
            ``data = {``
            ``       'CityRef' : 'db5c88d7-391c-11dd-90d9-001a92567626',``
            ``       'CounterpartyProperty' : 'Recipient',``
            ``       'CounterpartyType' : 'PrivatePerson',``
            ``       'Email' : '',``
            ``       'FirstName' : 'Андрій',``
            ``       'LastName' : 'Яковлєв',``
            ``       'MiddleName' : 'Адуардович',``
            ``       'Phone' : '0997979789' }``
            ``counterparty.save(from_data=data)``

        :param from_data:
            dictionary with all required data, will be used instead of passing each keyword separately
        :param city_ref:
            ID of the counterparty's city
        :type city_ref:
            str or unicode
        :param first_name:
            first name of the counterparty
        :type:
            str or unicode
        :param mid_name:
            middle name of the counterparty
        :type:
            str or unicode
        :param last_name:
            last name of the counterparty
        :type:
            str or unicode
        :param phone:
            phone number of the counterparty
        :type:
            str or unicode
        :param email:
            e-mail address of the counterparty
        :type:
            str or unicode
        :param cp_type:
            type of the counterparty (`PrivatePerson` etc.)
        :type:
            str or unicode
        :param cp_prop:
            counterparty property (can be either `Sender` or `Recipient`)
        :type:
            str or unicode
        :return:
            dictionary with info about saved counterparty
        :rtype:
            dict
        """
        if from_data:
            props = from_data
        else:
            props = {
                'CityRef': city_ref,
                'FirstName': first_name,
                'MiddleName': mid_name,
                'LastName': last_name,
                'Phone': phone,
                'Email': email,
                'CounterpartyType': cp_type,
                'CounterpartyProperty': cp_prop
            }
        req = self.send(method='save', method_props=props)
        return req

    # TODO: API requires all fields to be passed. Maybe we can pre-fetch data from API and use if no need to update it
    def update(self,
               from_data=None,
               cp_ref=None,
               city_ref=None,
               first_name=None,
               mid_name=None,
               last_name=None,
               phone=None,
               email=None,
               cp_type=None,
               cp_prop=None,
               own_form=None):
        """
        Method for updating counterparty. All fields are required
        Named arguments can be used or it is possible to update pre-parsed dictionary with counterparty info.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.update(ref='db5c88d7-391c-11dd-90d9-001a92567626',``
            ``city_ref='db5c88d7-391c-11dd-90d9-001a92567626', first_name=u'Фелікс',``
            ``mid_name=u'Едуардович', last_name=u'Ковальчук', phone='0937979489',``
            ``email='myemail@my.com', cp_type='PrivatePerson', cp_prop='Recipient', own_form='')``
            or:
            ``counterparty = Counterparty()``
            ``data = {'Ref': 'db5c88d7-391c-11dd-90d9-001a92567626',``
            ``       'CityRef' : 'db5c88d7-391c-11dd-90d9-001a92567626',``
            ``       'CounterpartyProperty' : 'Recipient',``
            ``       'CounterpartyType' : 'PrivatePerson',``
            ``       'Email' : '',``
            ``       'FirstName' : 'Андрій',``
            ``       'LastName' : 'Яковлєв',``
            ``       'MiddleName' : 'Едуардович',``
            ``       'Phone' : '0997979789',``
            ``       'OwnershipForm': '' }``
            ``counterparty.update(from_data=data)``

        :param from_data:
            dictionary with all required data, will be used instead of passing each keyword separately
        :type from_data:
            dict
        :param city_ref:
            ID of the counterparty's city
        :type city_ref:
            str or unicode
        :param first_name:
            first name of the counterparty
        :type:
            str or unicode
        :param mid_name:
            middle name of the counterparty
        :type:
            str or unicode
        :param last_name:
            last name of the counterparty
        :type:
            str or unicode
        :param phone:
            phone number of the counterparty
        :type:
            str or unicode
        :param email:
            e-mail address of the counterparty
        :type:
            str or unicode
        :param cp_type:
            type of the counterparty (`PrivatePerson` etc.)
        :type:
            str or unicode
        :param cp_prop:
            counterparty property (can be either `Sender` or `Recipient`)
        :type:
            str or unicode
        :param own_form:
            ownership form of the counterparty.
            if needed, `get_ownership_forms_list`method from Common class can be used to get possible values
        :type own_form:
            str or unicode
        :return:
            dictionary with info about saved counterparty
        :rtype:
            dict
        """
        if from_data:
            props = from_data
        else:
            props = {
                'Ref': cp_ref,
                'CityRef': city_ref,
                'FirstName': first_name,
                'MiddleName': mid_name,
                'LastName': last_name,
                'Phone': phone,
                'Email': email,
                'CounterpartyType': cp_type,
                'CounterpartyProperty': cp_prop,
                'OwnershipForm': own_form
            }
        req = self.send(method='update', method_props=props)
        return req

    def delete(self, cp_ref):
        """
        Method for deleting counterparties.
        Due to restrictions, only `Recipient` counterparty type can be deleted.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.delete('342e8add-6953-11e5-ad08-005056801333')``
        :param cp_ref:
            ID of the counterparty
        :type cp_ref:
            str or unicode
        :return:
            dictionary with ID of deleted counterparty
        """
        req = self.send(method='delete', method_props={'Ref': cp_ref})
        return req

    # def save_third_person(self):
    #     """Not implemented due to contract lack, will be here in the future. Maybe :)"""
    #     return False

    def get_counterparty_options(self, cp_ref):
        """
        Method for getting counterparties options.

        :example:
            ``counterparty = Counterparty()``
            ``counterparty.get_counterparty_options('342e8add-6953-11e5-ad08-005056801333')``
        :param cp_ref:
            ID of the counterparty
        :type:
            str or unicode
        :return:
            dictionary with counterparty's options
        """
        req = self.send(method='getCounterpartyOptions', method_props={'Ref': cp_ref})
        return req


class Common(NovaPoshtaApi):
    """A class representing the `Common` model of Nova Poshta API.
    Used for parsing common (obviously) information, which represents different data (cargo, payment etc.).
    """

    def get_types_of_payers(self):
        """
        Method for fetching info about types of payers.

        :example:
            ``common = Common()``
            ``common.get_types_of_payers()``
        :return:
            dictionary with info about types of payers
        """
        req = self.send(method='getTypesOfPayers')
        return req

    def get_payment_forms(self):
        """
        Method for fetching info about possible payment forms.

        :example:
            ``common = Common()``
            ``common.get_payment_forms()``
        :return:
            dictionary with info about payment forms
        :rtype:
            dict
        """
        req = self.send(method='getPaymentForms')
        return req

    def get_cargo_types(self):
        """
        Method for fetching info about cargo types.

        :example:
            ``common = Common()``
            ``common.get_cargo_types()``
        :return:
            dictionary with info about cargo types
        :rtype:
            dict
        """
        req = self.send(method='getCargoTypes')
        return req

    def get_service_types(self):
        """
        Method for fetching info about possible delivery methods.

        :example:
            ``common = Common()``
            ``common.get_service_types()``
        :return:
            dictionary with info about possible delivery methods
        :rtype:
            dict
        """
        req = self.send(method='getServiceTypes')
        return req

    def get_cargo_description_list(self):
        """
        Method for fetching the directory of cargo description.

        :example:
            ``common = Common()``
            ``common.get_cargo_description_list()``
        :return:
            dictionary with cargo descriptions
        :rtype:
            dict
        """
        req = self.send(method='getCargoDescriptionList')
        return req

    def search_cargo_description_list(self, keyword):
        """
        Method for fetching cargo description by keyword.
        In general, it is extended version of `get_cargo_description_list` with `FindByString` API's methods param.
        :example:
            ``common = Common()``
            ``common.search_cargo_description_list(u'Абажур')``
        :param keyword:
            keyword for searching
        :type keyword:
            str or unicode
        :return:
            dictionary with cargo descriptions
        :rtype:
            dict
        """
        req = self.send(method='getCargoDescriptionList', method_props={'FindByString': keyword})
        return req

    def get_ownership_forms_list(self):
        """
        Method for fetching info about ownership forms.

        :example:
            ``common = Common()``
            ``common.get_ownership_forms_list()``
        :return:
            dictionary with info about ownership forms
        :rtype:
            dict
        """
        req = self.send(method='getOwnershipFormsList')
        return req

    def get_backward_delivery_cargo_types(self):
        """
        Method for fetching info about backward delivery cargo types.

        :example:
            ``common = Common()``
            ``common.get_backward_delivery_cargo_types()``
        :return:
            Dictionary with info about backward delivery cargo types.
        :rtype:
            dict
        """
        req = self.send('getBackwardDeliveryCargoTypes')
        return req

    def get_pallets_list(self):
        """
        Method for fetching info about pallets for backward delivery.

        :example:
            ``common = Common()``
            ``common.get_pallets_list()``
        :return:
            dictionary with info about pallets
        :rtype:
            dict
        """
        req = self.send(method='getPalletsList')
        return req

    def get_type_of_counterparties(self):
        """
        Method for fetching info about types of counterparties.

        :example:
            ``common = Common()``
            ``common.get_type_of_counterparties()``
        :return:
            dictionary with info about types of counterparties
        :rtype:
            dict
        """
        req = self.send(method='getTypesOfCounterparties')
        return req

    def get_type_of_payers_for_redelivery(self):
        """
        Method for fetching info about types of payers for redelivery.

        :example:
            ``common = Common()``
            ``common.get_type_of_payers_for_redelivery()``
        :return:
            dictionary with info about types of payers for redelivery
        :rtype:
            dict
        """
        req = self.send(method='getTypesOfPayersForRedelivery')
        return req

    def ex_get_time_intervals(self, city, datetime):
        """
        Method for fetching info about time intervals (for ordering "time intervals" service).
        Extended version of `get_time_intervals`.
        City name is used instead of ID.

        :example:
        ``common = Common()``
        ``common.ex_get_time_intervals(city=u'Рівне', datetime=u'2.10.2015')``
        :param city:
            name of the recipient's city
        :param datetime:
            date for getting info about time intervals ('dd.mm.yyyy' date format)
        :return:
            dictionary with info about time intervals
        :rtype:
            dict
        """
        city_ref = Address().get_city_by_name(city)['data'][0]['Ref']
        req = self.send(method='getTimeIntervals', method_props={'RecipientCityRef': city_ref, 'DateTime': datetime})
        return req

    def get_time_intervals(self, city_ref, datetime):
        """
        Method for fetching info about time intervals (for ordering "time intervals" service).

        :example:
        ``common = Common()``
        ``common.get_time_intervals(city_ref=u'udb5c896a-391c-11dd-90d9-001a92567626', datetime=u'2.10.2015')``
        :param city_ref:
            ID of the recipient's city
        :param datetime:
            date for getting info about time intervals ('dd.mm.yyyy' date format)
        :return:
            dictionary with info about time intervals
        :rtype:
            dict
        """
        req = self.send(method='getTimeIntervals', method_props={'RecipientCityRef': city_ref, 'DateTime': datetime})
        return req

    def get_tires_wheels_list(self):
        """
        Method for fetching info about tires and wheels (if cargo is "tires-wheels").

        :example:
            ``common = Common()``
            ``common.get_tires_wheels_list()``
        :return:
            dictionary with info about tires and wheels
        :rtype:
            dict
        """
        req = self.send(method='getTiresWheelsList')
        return req

    def get_trays_list(self):
        """
        Method for fetching info about trays (if backward delivery is ordered).

        :example:
            ``common = Common()``
            ``common.get_trays_list()``
        :return:
            dictionary with info about trays
        :rtype:
            dict
        """
        req = self.send(method='getTraysList')
        return req

    def get_document_statuses(self):
        """
        Method for fetching info about statuses of documents.

        :example:
            ``common = Common()``
            ``common.get_document_statuses()``
        :return:
            dictionary with info about statuses of documents
        :rtype:
            dict
        """
        req = self.send(method='getDocumentStatuses')
        return req

    def get_document_status(self, state_id=None, group_id=None, state_name=None):
        """
        Method for fetching info about status of one document.
        Can be filtered by several params (one or many).
        Since there is no default values, at least one filter should be used.

        :example:
            ``common = Common()``
            ``common.get_document_status(state_id=u'1')
            ``common.get_document_status(group_id=u'1')``
            ``common.get_document_status(group_id=u'1')
            ``common.get_document_status(state_name=u'Замовлення в обробці')
            ``common.get_document_status(group_id=u'1', state_name=u'Замовлення в обробці')

        :param state_id:
            numeric ID of document status
        :type state_id:
            str or unicode
        :param group_id:
            numeric group ID of document status
        :type state_name:
            str or unicode
        :param state_name:
            name of the status
        :type:
            str or unicode
        :return:
            dict with info about status of one document
        """
        filter_by = {
            'StateId': state_id,
            'GroupId': group_id,
            'StateName': state_name
        }
        req = self.send(method='getDocumentStatuses', method_props=filter_by)
        return req


class ContactPerson(NovaPoshtaApi):
    pass
