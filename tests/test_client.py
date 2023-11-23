from novaposhta.client import NovaPoshtaApi, InvalidAPIKeyError, APIRequestError
from tests.helpers import TEST_URI, TEST_API_KEY, MockModel
import pytest


def test_client_send(httpx_mock):
    json_response = {"success": True}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)
    response = client.send("test", "test", {})

    assert response == json_response


def test_client_send_with_raise_for_errors_and_success(httpx_mock):
    json_response = {"success": True}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, raise_for_errors=True)
    response = client.send("test", "test", {})

    assert response == json_response


def test_client_send_with_raise_for_errors_and_key_problem(httpx_mock):
    json_response = {"success": False, "errors": ["API key error"]}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, raise_for_errors=True)
    with pytest.raises(InvalidAPIKeyError):
        client.send("test", "test", {})


def test_client_send_with_raise_for_errors_and_other_problem(httpx_mock):
    json_response = {"success": False, "errors": ["Some kind of error"]}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, raise_for_errors=True)
    with pytest.raises(APIRequestError):
        client.send("test", "test", {})


def test_client_new_get(httpx_mock):
    json_response = {"success": True}

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


@pytest.mark.asyncio
async def test_async_client_new_get(httpx_mock):
    json_response = {"OK": 200}

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, async_mode=True)
    model = client.new(MockModel)
    saved_model = client.get(MockModel.name)

    assert model == saved_model
    assert await model.test() == json_response
