# novaposhta-python-client

A Python client for interfacing with the Nova Poshta API. Designed to provide easy access to all API functionalities
with emphasis on consistency and usability.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


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
```

You can also use async client:

```python
import asyncio
from novaposhta.client import NovaPoshtaApi

async_client = NovaPoshtaApi('my-api-token', timeout=30, async_mode=True)
a_address = async_client.address
a_settlement = asyncio.run(a_address.search_settlements(city_name='Київ', limit=5))
print(a_settlement)
```

## Error handling

```python
import httpx
from novaposhta.client import NovaPoshtaApi, InvalidAPIKeyError, APIRequestError

# Instantiate the client
client = NovaPoshtaApi('my-api-token', timeout=30, raise_for_errors=True)

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

client = NovaPoshtaApi('my-api-token', http_client=my_http_client.Client)
```

Custom client should support context manager, e.g:

```python
with self.http_client() as client:
    response = client.post(
        self.api_endpoint, json=request, headers=HEADERS, timeout=self.timeout
    )
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

## Testing and linting

```bash
poetry run black novaposhta
poetry run mypy novaposhta/
poetry run pytest tests/
```

## Contributing

We welcome contributions that can help in enhancing the functionality and improving the consistency of the client. For
bugs or feature requests, please open an issue on the GitHub repository.
Please, use `black` and `mypy` as your instrument for code formatting and type checking.
