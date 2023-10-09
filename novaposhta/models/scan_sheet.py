"""ScanSheet model module."""

from novaposhta.models.base import BaseModel, api_method
from typing import List


class ScanSheet(BaseModel):
    name = "ScanSheet"

    def __init__(self, client):
        super().__init__(client)

    @api_method("insertDocuments")
    def insert_documents(self, document_refs: List[str], ref: str, date: str):
        return self._call_with_props(DocumentRefs=document_refs, Ref=ref, Date=date)

    @api_method("getScanSheet")
    def get_scan_sheet(self, ref: str, counterparty_ref: str):
        return self._call_with_props(Ref=ref, CounterpartyRef=counterparty_ref)

    @api_method("getScanSheetList")
    def get_scan_sheet_list(self):
        return self._call_with_props()

    @api_method("deleteScanSheet")
    def delete_scan_sheet(self, scan_sheet_refs: List[str]):
        return self._call_with_props(ScanSheetRefs=scan_sheet_refs)

    @api_method("removeDocuments")
    def remove_documents(self, document_refs: List[str], ref: str):
        return self._call_with_props(DocumentRefs=document_refs, Ref=ref)
