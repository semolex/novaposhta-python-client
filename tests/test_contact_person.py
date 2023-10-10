import pytest

from novaposhta.models.contact_person import ContactPerson
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
            "counterparty_ref": "counterparty_ref",
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
            "phone": "phone",
            "email": "email",
            "counterparty_ref": "counterparty_ref",
        },
        "expected": "expected_response",
    },
    {"method": "delete", "params": {"ref": "ref"}, "expected": "expected_response"},
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_contact_person(test_input, httpx_mock):
    method_test(ContactPerson, test_input, httpx_mock)
