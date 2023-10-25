import pytest

from novaposhta.models.internet_document import InternetDocument
from tests.helpers import method_test

methods_to_test = [
    {
        "method": "get_document_price",
        "params": {
            "city_sender": "8d5a980d-391c-11dd-90d9-001a92567626",
            "city_recipient": "db5c88f0-391c-11dd-90d9-001a92567626",
            "service_type": "WarehouseWarehouse",
            "weight": 10,
            "cost": 1000,
            "seats_amount": 1,
            "cargo_type": "Cargo",
        },
        "expected": "expected_response",
    },
    {
        "method": "get_document_delivery_date",
        "params": {
            "city_sender": "8d5a980d-391c-11dd-90d9-001a92567626",
            "city_recipient": "db5c88f0-391c-11dd-90d9-001a92567626",
            "service_type": "WarehouseWarehouse",
        },
        "expected": "expected_response",
    },
    {"method": "save", "params": {}, "expected": "expected_response"},
    {
        "method": "update",
        "params": {
            "ref": "ref",
            "payer_type": "Sender",
            "payment_method": "Cash",
            "date_time": "datetime",
            "city_recipient": "db5c88f0-391c-11dd-90d9-001a92567626",
            "cargo_type": "Cargo",
            "weight": 10,
            "service_type": "WarehouseWarehouse",
            "seats_amount": 1,
            "description": "description",
            "cost": 1000,
            "city_sender": "8d5a980d-391c-11dd-90d9-001a92567626",
            "sender": "sender",
            "sender_address": "sender_address",
            "contact_sender": "contact_sender",
            "senders_phone": "senders_phone",
            "recipient": "recipient",
            "recipient_address": "recipient_address",
            "contact_recipient": "contact_recipient",
            "recipients_phone": "recipients_phone",
            "volume_general": 1,
        },
        "expected": "expected_response",
    },
    {
        "method": "get_document_list",
        "params": {"date_time_from": "date_time_from", "date_time_to": "date_time_to"},
        "expected": "expected_response",
    },
    {
        "method": "get_incoming_documents_by_phone",
        "params": {
            "date_from": "24.10.2023 00:00:00",
            "date_to": "25.10.2023 00:00:00",
            "limit": 100,
        },
        "expected": "expected_response",
    },
    {
        "method": "delete",
        "params": {"document_refs": "ref"},
        "expected": "expected_response",
    },
    {
        "method": "generate_report",
        "params": {
            "document_refs": ["ref1", "ref2"],
            "_type": "pdf",
            "date_time": "date_time",
        },
        "expected": "expected_response",
    },
]


@pytest.mark.parametrize("test_input", methods_to_test)
def test_internet_document(test_input, httpx_mock):
    method_test(InternetDocument, test_input, httpx_mock)
