"""ScanSheet model module."""

from .base import BaseModel, api_method
from typing import List


class ScanSheet(BaseModel):
    """
    ScanSheet model class.
    """

    name = "ScanSheet"

    def __init__(self, client):
        super().__init__(client)

    @api_method("insertDocuments")
    def insert_documents(self, document_refs: List[str], ref: str, date: str):
        """
        Insert documents.

        :param document_refs: document references.
        :param ref: reference.
        :param date: date.
        :return: response dict.
        """
        return self._call_with_props(DocumentRefs=document_refs, Ref=ref, Date=date)

    @api_method("getScanSheet")
    def get_scan_sheet(self, ref: str, counterparty_ref: str):
        """
        Get scan sheet.

        :param ref: reference.
        :param counterparty_ref: counterparty reference.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref, CounterpartyRef=counterparty_ref)

    @api_method("getScanSheetList")
    def get_scan_sheet_list(self):
        """
        Get scan sheet list.
        """
        return self._call_with_props()

    @api_method("deleteScanSheet")
    def delete_scan_sheet(self, scan_sheet_refs: List[str]):
        """
        Delete scan sheet.

        :param scan_sheet_refs: scan sheet references.
        """
        return self._call_with_props(ScanSheetRefs=scan_sheet_refs)

    @api_method("removeDocuments")
    def remove_documents(self, document_refs: List[str], ref: str):
        """
        Remove documents.

        :param document_refs: document references.
        :param ref: reference.
        """
        return self._call_with_props(DocumentRefs=document_refs, Ref=ref)
