"""TrackingDocument model module."""

from novaposhta.models.base import BaseModel, api_method

from typing import List, Dict


class TrackingDocument(BaseModel):
    name = "TrackingDocument"

    def __init__(self, client):
        super().__init__(client)

    @api_method("getStatusDocuments")
    def get_status_documents(self, documents: List[Dict[str, str]]):
        return self._call_with_props(Documents=documents)
