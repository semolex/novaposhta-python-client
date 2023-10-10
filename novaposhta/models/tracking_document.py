"""TrackingDocument model module."""

from .base import BaseModel, api_method

from typing import List, Dict


class TrackingDocument(BaseModel):
    """
    TrackingDocument model class.
    """

    name = "TrackingDocument"

    def __init__(self, client):
        super().__init__(client)

    @api_method("getStatusDocuments")
    def get_status_documents(self, documents: List[Dict[str, str]]):
        """
        Get status documents.

        :param documents: list of documents.
        :return: response dict.
        """
        return self._call_with_props(Documents=documents)
