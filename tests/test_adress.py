import pytest

from novaposhta.models.address import Address
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "search_settlements",
        "params": {"city_name": "Kyiv", "limit": 5, "page": 1},
        "expected": "expected_response",
    },
    {
        "method": "search_settlement_streets",
        "params": {"street_name": "Khreshchatyk", "settlement_ref": "ref", "limit": 5},
        "expected": "expected_response",
    },
    {
        "method": "save",
        "params": {
            "counterparty_ref": "ref",
            "street_ref": "ref",
            "building_number": "1",
            "flat": "1",
            "note": "note",
        },
        "expected": "expected_response",
    },
    {
        "method": "update",
        "params": {
            "ref": "ref",
            "counterparty_ref": "ref",
            "street_ref": "ref",
            "building_number": "1",
            "flat": "1",
            "note": "note",
        },
        "expected": "expected_response",
    },
    {"method": "delete", "params": {"ref": "ref"}, "expected": "expected_response"},
    {"method": "get_areas", "params": {}, "expected": "expected_response"},
    {"method": "get_cities", "params": {}, "expected": "expected_response"},
    {"method": "get_settlements", "params": {}, "expected": "expected_response"},
    {
        "method": "get_warehouses",
        "params": {"bicycle_parking": True, "post_finance": True},
        "expected": "expected_response",
    },
    {"method": "get_warehouse_types", "params": {}, "expected": "expected_response"},
    {
        "method": "get_street",
        "params": {"city_ref": "ref", "find_by_string": "string"},
        "expected": "expected_response",
    },
    {"method": "get_warehouse_types", "params": {}, "expected": "expected_response"},
    {
        "method": "get_settlement_country_region",
        "params": {"area_ref": "ref"},
        "expected": "expected_response",
    },
    {
        "method": "get_settlement_areas",
        "params": {"ref": "ref"},
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_address(test_input, httpx_mock):
    method_test(Address, test_input, httpx_mock)
