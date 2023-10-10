import pytest

from novaposhta.models.common import Common
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "get_time_intervals",
        "params": {"recipient_city_ref": "8d5a980d-391c-11dd-90d9-001a92567626"},
        "expected": "expected_response",
    },
    {"method": "get_cargo_types", "params": {}, "expected": "expected_response"},
    {
        "method": "get_backward_delivery_cargo_types",
        "params": {},
        "expected": "expected_response",
    },
    {"method": "get_pallets_list", "params": {}, "expected": "expected_response"},
    {
        "method": "get_types_of_payers_for_redelivery",
        "params": {},
        "expected": "expected_response",
    },
    {"method": "get_pack_list", "params": {}, "expected": "expected_response"},
    {"method": "get_tires_wheels_list", "params": {}, "expected": "expected_response"},
    {
        "method": "get_cargo_description_list",
        "params": {},
        "expected": "expected_response",
    },
    {"method": "get_message_code_text", "params": {}, "expected": "expected_response"},
    {"method": "get_service_types", "params": {}, "expected": "expected_response"},
    {
        "method": "get_ownership_forms_list",
        "params": {},
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_common(test_input, httpx_mock):
    method_test(Common, test_input, httpx_mock)
