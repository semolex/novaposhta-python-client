import pytest

from novaposhta.models.scan_sheet import ScanSheet
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "insert_documents",
        "params": {"document_refs": ["ref"], "ref": "ref", "date": "date"},
        "expected": "expected_response",
    },
    {
        "method": "get_scan_sheet",
        "params": {"ref": "ref", "counterparty_ref": "ref"},
        "expected": "expected_response",
    },
    {"method": "get_scan_sheet_list", "params": {}, "expected": "expected_response"},
    {
        "method": "delete_scan_sheet",
        "params": {"scan_sheet_refs": ["ref"]},
        "expected": "expected_response",
    },
    {
        "method": "remove_documents",
        "params": {"document_refs": ["ref"], "ref": "ref"},
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_scan_sheet(test_input, httpx_mock):
    method_test(ScanSheet, test_input, httpx_mock)
