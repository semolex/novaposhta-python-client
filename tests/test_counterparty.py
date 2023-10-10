import pytest

from novaposhta.models.counterparty import Counterparty
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "save",
        "params": {
            "first_name": "first_name",
            "middle_name": "middle_name",
            "last_name": "last_name",
            "phone": "phone",
            "email": "email",
            "counterparty_type": "counterparty_type",
            "edrpou": "edrpou",
            "counterparty_property": "counterparty_property",
            "city_ref": "city_ref",
        },
        "expected": "expected_response",
    },
    {
        "method": "update",
        "params": {
            "ref": "ref",
            "first_name": "first_name",
            "middle_name": "middle_name",
            "last_name": "last_name",
            "counterparty_type": "counterparty_type",
            "counterparty_property": "counterparty_property",
            "city_ref": "city_ref",
        },
        "expected": "expected_response",
    },
    {"method": "delete", "params": {"ref": "ref"}, "expected": "expected_response"},
    {
        "method": "get_counterparty_addresses",
        "params": {"ref": "ref"},
        "expected": "expected_response",
    },
    {
        "method": "get_counterparty_options",
        "params": {"ref": "ref"},
        "expected": "expected_response",
    },
    {
        "method": "get_counterparty_contact_persons",
        "params": {"ref": "ref"},
        "expected": "expected_response",
    },
    {
        "method": "get_counterparties",
        "params": {"counterparty_property": "counterparty_property"},
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("method_to_test", methods_to_test)
def test_counterparty(method_to_test, httpx_mock):
    method_test(Counterparty, method_to_test, httpx_mock)
