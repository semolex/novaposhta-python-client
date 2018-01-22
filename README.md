# novaposhta-api-client
Python client for Nova Poshta company's API.
## Installation
Client is based on `python 3.6`.

You can install package by using pip:
 
`pip install git+https://github.com/semolex/novaposhta-api-client`

## Description
Client is based on models and signatures, provided in [NovaPoshta API documentation](https://devcenter.novaposhta.ua/docs/services/).

Main idea of the client is to provide same methods as described there with minimal
changes when it possible.

Methods and they parameters in most cases shares same names as in API docs, but 
in python-like style.

However, some models are omitted due to their singleton nature, for example,
`AddressGeneral` model is part of the `AddressModel`, because it has only one 
method and semantically it is definitely part of the address-related items, etc.
You can explore source code to find this parts.

Also, while there methods are designed to wrap same methods from API, there is 
may be some different and additions. 

For example, some methods may be divided into 
smaller logical parts, because they uses _a lot_ of parameters, also there is 
additional classes (`WarehouseFilter` and `ExpressWaybill`), used to divide 
some properties as separate class that can be passed to the method that will 
extract required parts.

There is a plans to add more logical chunks, so user can have different ways of
manipulating complex parts.

## Usage
To start using client, you need to have API key.

Methods returns `requests.Response` object so you have ability to add different 
checks and conversions, eg. check status codes, describe errors, warnings, etc.

Simple usage example:
```python
from novaposhta import NovaPoshtaApi
# call api by using corresponding models
client = NovaPoshtaApi(api_key='your-api-key')
areas = client.address.get_areas() # models can be accessed as client properties
print(areas.json())

# call api by using `send` method from client.
reasons = client.send('AdditionalService', 'getReturnReasons', {})
print(reasons.json())

# you can pass parameters into method using two different ways.
# 1. Pass them directly.
cities_one = client.address.search_settlements(city_name='Здолбунів', limit=5)
# 2. Prepare required object as dictionary and unpack it.
query = {
    'city_name': 'Здолбунів',
    'limit': 5
}
cities_two = client.address.search_settlements(**query)
```

## Plans to add before release version:
* Add name mappings, so user can pass JSON object with same property names as in API docs.
  (eg. `AddressCity` can be used in dict object and then automatically converted into `address_city`)
* Create test parts
* Double check existing parameters, because API docs missing some small parts.
* Add more classes that can represent data chunks so it will be possible to manipulate big objects easily.
