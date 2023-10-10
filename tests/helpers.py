from novaposhta.models.base import BaseModel, api_method
from novaposhta.client import NovaPoshtaApi

TEST_URI = "https://api.test-novaposhta.ua/v2.0/json/"
TEST_API_KEY = "test"


class MockModel(BaseModel):
    name = "MockModel"

    def __init__(self, client):
        super().__init__(client)

    @api_method("test")
    def test(self):
        return self._call_with_props()


def method_test(model, test_input, httpx_mock):
    client_instance = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)

    address_instance = model(client_instance)

    httpx_mock.add_response(json=test_input["expected"])

    method = getattr(address_instance, test_input["method"])

    response = method(**test_input["params"])

    assert response == test_input["expected"]
