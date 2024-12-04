import pytest

from novaposhta.client import (APIRequestError, InvalidAPIKeyError,
                               NovaPoshtaApi)
from tests.helpers import TEST_API_KEY, TEST_URI, MockModel


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


def test_client_unexpected_error_format(httpx_mock):
    json_response = {
        "success": False,
        "errors": {"0": "Some kind of error", "1": "Another error"},
    }

    httpx_mock.add_response(json=json_response, status_code=200)

    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, raise_for_errors=True)
    model = client.new(MockModel)
    with pytest.raises(APIRequestError):
        model.test()


def test_client_context_manager(httpx_mock):
    json_response = {"success": True}

    httpx_mock.add_response(json=json_response, status_code=200)

    with NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI) as client:
        model = client.new(MockModel)
        saved_model = client.get(MockModel.name)

        assert model == saved_model
        assert model.test() == json_response
    assert client.sync_http_client.is_closed


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


@pytest.mark.asyncio
async def test_async_client_context_manager(httpx_mock):
    json_response = {"OK": 200}

    httpx_mock.add_response(json=json_response, status_code=200)

    async with NovaPoshtaApi(
            TEST_API_KEY, api_endpoint=TEST_URI, async_mode=True
    ) as client:
        model = client.new(MockModel)
        saved_model = client.get(MockModel.name)

        assert model == saved_model
        assert await model.test() == json_response
    assert client.async_http_client.is_closed


def test_client_init_validation():
    with pytest.raises(ValueError):
        NovaPoshtaApi(None, api_endpoint=TEST_URI)
    with pytest.raises(ValueError):
        NovaPoshtaApi("", api_endpoint=TEST_URI)
    with pytest.raises(ValueError):
        NovaPoshtaApi(TEST_API_KEY, api_endpoint=None)
    with pytest.raises(ValueError):
        NovaPoshtaApi(TEST_API_KEY, api_endpoint="")
    with pytest.raises(ValueError):
        NovaPoshtaApi(TEST_API_KEY, api_endpoint="tcp://localhost")
    with pytest.raises(ValueError):
        NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, timeout=-1)
    with pytest.raises(ValueError):
        NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, timeout=0)
    with pytest.raises(ValueError):
        NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, timeout=0, async_mode=True)


@pytest.mark.asyncio
async def test_client_fails_on_async_call_with_sync_client(httpx_mock):
    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI)
    with pytest.raises(ValueError) as e:
        req = {"url": TEST_URI, "json": {}}
        await client._send_async(req)
    assert "Async client is not initialized" in str(e.value)


def test_client_fails_on_sync_call_with_async_client(httpx_mock):
    client = NovaPoshtaApi(TEST_API_KEY, api_endpoint=TEST_URI, async_mode=True)
    with pytest.raises(ValueError) as e:
        req = {"url": TEST_URI, "json": {}}
        client._send_sync(req)
    assert "Sync client is not initialized" in str(e.value)
