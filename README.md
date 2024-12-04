# novaposhta-python-client

A Python client for interfacing with the Nova Poshta API. Designed to provide easy access to all API functionalities
with emphasis on consistency and usability.

[![Tests](https://github.com/semolex/novaposhta-python-client/actions/workflows/tests.yml/badge.svg)](https://github.com/semolex/novaposhta-python-client/actions/workflows/tests.yml)
[![License](https://img.shields.io/github/license/semolex/novaposhta-python-client)](https://github.com/semolex/novaposhta-python-client/blob/master/LICENSE.md)
[![PyPI](https://img.shields.io/pypi/v/novaposhta-python-client)](https://pypi.org/project/novaposhta-python-client/)
[![Downloads](https://pepy.tech/badge/novaposhta-python-client)](https://pepy.tech/project/novaposhta-python-client)
[![Downloads](https://pepy.tech/badge/novaposhta-python-client/month)](https://pepy.tech/project/novaposhta-python-client)
[![Python Versions](https://img.shields.io/pypi/pyversions/novaposhta-python-client.svg)](https://pypi.org/project/novaposhta-python-client/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)

## Description

This client is compatible with `python = "^3.9"` and aims to mirror the Nova Poshta API's endpoints, offering a 1:1
mapping where possible. However, users should be aware of the inconsistencies and occasional ambiguities present in the
API. This can affect the signatures of some methods, and special attention is needed when working with endpoints like
the `save` method from some models which can create different items based on the provided input.

Efforts to enhance the consistency and robustness of the client are ongoing, and future releases will focus on thorough
testing and refinement of all possible parameter combinations.

## Installation

```bash
pip install novaposhta-python-client
```

## Usage

Here's a basic example of how to use the client:

```python
from novaposhta.client import NovaPoshtaApi

# Instantiate the client
client = NovaPoshtaApi('my-api-token', timeout=30)

# Example usage of different models
settlements = client.address.search_settlements(city_name='Київ', limit=5)
my_pack_list = client.common.get_pack_list(length=1, width=5)
return_reason = client.additional_service.get_return_reasons()

# Print results
print(settlements, my_pack_list, return_reason)
client.close_sync()
```
Please, close the client whenever you are done with it to avoid resource leaks.

You can also use async client:

```python
import asyncio
from novaposhta.client import NovaPoshtaApi

async def use_api_async():
    async_client = NovaPoshtaApi('your_api_key', timeout=30, async_mode=True, raise_for_errors=True)
    address = async_client.address
    settlements = await address.search_settlements(city_name='Київ', limit=5)
    print(settlements)
    await async_client.close_async()
asyncio.run(use_api_async())
```

You can use context manager to automatically close the client:

```python
from novaposhta.client import NovaPoshtaApi
def use_api_sync():
    with NovaPoshtaApi(api_key='your_api_key', async_mode=False) as api:
        # Do something with the API
        pass

async def use_api_async():
    async with NovaPoshtaApi(api_key='your_api_key', async_mode=True) as api:
        # Do something with the API
        pass
```

## Error handling

```python
import httpx
from novaposhta.client import NovaPoshtaApi, InvalidAPIKeyError, APIRequestError

# Instantiate the client
client = NovaPoshtaApi('your_api_key', timeout=30, raise_for_errors=True)

try:
    client.common.get_cargo_types()
except httpx.HTTPError as error:
    print(f"HTTP error: {error}")
except InvalidAPIKeyError as error:
    print(f"API key expired or otherwise invalid: {error}")
except APIRequestError as error:
    print(f"Something else is wrong with API request: {error}")
```

## Extending the Client

### Custom HTTP Client

While `httpx` is the default HTTP library, you can easily substitute it with requests or another library, provided it
follows the same interface:

```python
from novaposhta.client import NovaPoshtaApi
import my_http_client

client = NovaPoshtaApi('your_api_key', http_client=my_http_client.Client)
```

### Adding New Methods

If a method isn’t implemented, or you prefer a custom implementation, extend the model as shown below:

```python
from novaposhta.models.base import BaseModel, api_method


class MyCustomModel(BaseModel):
    @api_method('MissingMethod')
    def missing_method(self, some_param: str):
        return self._call_with_props(SomeParam=some_param)
```

The client caches all model instances. To reset and create a new model instance, use the new method:

```python
from novaposhta.client import NovaPoshtaApi
from novaposhta.models.address import Address

client = NovaPoshtaApi('my-api-token')
address = client.new(Address)
```

To get your custom model instance, use the get method:

```python
my_custom_model = client.get(MyCustomModel.name)
```

## Experimental: Chain Operations

The chain functionality allows you to sequence multiple API operations, where each operation's output can be transformed and passed to the next operation. This is particularly useful for scenarios that require multiple dependent API calls, like searching for addresses or creating shipments.
Each result of `prepare_next` is passed to the next operation as updated `kwargs`.
> ⚠️ **Note**: This feature is experimental and currently optimized for async usage.

### Basic Usage

```python
from novaposhta.client import NovaPoshtaApi
from novaposhta.chains import Chain 

# Initialize client in async mode
client = NovaPoshtaApi("API_KEY", async_mode=True)

# Create a chain of operations
chain = (
    Chain(
        client.address.get_areas,
        prepare_next=lambda x: {'ref': x['data'][0]['AreasCenter']}
    ) |
    Chain(
        client.address.get_cities,
        prepare_next=lambda x: {'city_ref': x['data'][0]['Ref']}
    ) |
    Chain(
        client.address.get_street,
        kwargs={'find_by_string': 'Street Name'}
    )
)

# Execute chain
results = await chain.execute_async()
```

### Features

- Chain multiple API operations using the `|` operator
- Transform operation results for next operation using `prepare_next`
- Automatic error handling and chain interruption on failure
- Preserve both original API responses and transformed data
- Initial parameters via `kwargs`

### Common Patterns

```python
# Address search chain
from novaposhta.client import NovaPoshtaApi

client = NovaPoshtaApi("API_KEY", async_mode=True)
from novaposhta.chains import Chain
address = client.address
chain = (
    Chain(
        address.search_settlements,
        kwargs={'city_name': 'Київ'},
        prepare_next=lambda x: {'settlement_ref': x['data'][0]['Ref']}
    ) |
    Chain(
        address.search_settlement_streets,
        kwargs={'street_name': 'Main'}
    )
)

# Execute and process results
results = await chain.execute_async()
for result in results:
    print(f"Success: {result.success}")
    print(f"Data: {result.data}")
    print(f"Next kwargs: {result.next_kwargs}")
```

### Limitations

- Currently optimized for async usage
- Experimental API that may change
- Sequential execution only (no parallel operations)



## Testing and linting
Note: install dev dependencies first
```bash
poetry run black novaposhta/
poetry run isort novaposhta/
poetry run mypy novaposhta/
poetry run pytest --cov=novaposhta tests/
```

## Contributing

We welcome contributions that can help in enhancing the functionality and improving the consistency of the client. For
bugs or feature requests, please open an issue on the GitHub repository.
Please, use `black`, `isort` and `mypy` as your instrument for code formatting and type checking.
