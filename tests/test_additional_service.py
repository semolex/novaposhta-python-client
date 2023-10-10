import pytest

from novaposhta.models.additional_service import AdditionalService
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "check_possibility_create_return",
        "params": {"number": 1},
        "expected": "expected_response",
    },
    {"method": "get_return_reasons", "params": {}, "expected": "expected_response"},
    {
        "method": "get_return_reasons_subtypes",
        "params": {"reason_ref": "ref"},
        "expected": "expected_response",
    },
    {
        "method": "save",
        "params": {"int_doc_number": "1", "payment_method": "cash", "note": "note"},
        "expected": "expected_response",
    },
    {"method": "delete", "params": {"ref": "ref"}, "expected": "expected_response"},
    {
        "method": "get_return_orders_list",
        "params": {"page": 1, "limit": 5},
        "expected": "expected_response",
    },
    {"method": "delete", "params": {"ref": "ref"}, "expected": "expected_response"},
    {
        "method": "check_possibility_change_ew",
        "params": {"int_doc_number": 1},
        "expected": "expected_response",
    },
    {
        "method": "get_change_ew_orders_list",
        "params": {"begin_date": "date", "end_date": "date", "page": 1, "limit": 5},
        "expected": "expected_response",
    },
    {
        "method": "check_possibility_for_redirecting",
        "params": {"number": 1},
        "expected": "expected_response",
    },
    {
        "method": "get_redirection_orders_list",
        "params": {"begin_date": "date", "end_date": "date", "page": 1, "limit": 5},
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_additional_service(test_input, httpx_mock):
    method_test(AdditionalService, test_input, httpx_mock)
