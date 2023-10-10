import pytest

from novaposhta.models.tracking_document import TrackingDocument
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "get_status_documents",
        "params": {
            "documents": [{"DocumentNumber": "20400000000001", "Phone": "380000000000"}]
        },
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_tracking_document(test_input, httpx_mock):
    method_test(TrackingDocument, test_input, httpx_mock)
