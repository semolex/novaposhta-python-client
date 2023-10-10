from novaposhta.client import NovaPoshtaApi
from tests.helpers import TEST_URI, TEST_API_KEY, MockModel


def test_client_send(httpx_mock):
    json_response = {"test": "test"}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)
    response = client.send("test", "test", {})

    assert response == json_response


def test_client_new_get(httpx_mock):
    json_response = {"test": "test"}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)
    model = client.new(MockModel)
    saved_model = client.get(MockModel.name)

    assert model == saved_model
    assert model.test() == json_response


def test_client_reset():
    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)
    model = client.new(MockModel)
    saved_model = client.get(MockModel.name)
    assert str(model) == str(saved_model)

    assert model == saved_model
    reset_model = client.new(MockModel)
    assert reset_model != model


def test_has_models():
    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)

    assert client.additional_service
    assert client.address
    assert client.common
    assert client.contact_person
    assert client.counterparty
    assert client.internet_document
    assert client.scan_sheet
    assert client.tracking_document
