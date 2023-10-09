"""Counterparty model module."""

from novaposhta.models.base import BaseModel, api_method

from novaposhta.types import OptStr


class Counterparty(BaseModel):
    name = "Counterparty"

    def __init__(self, client):
        super().__init__(client)

    @api_method("save")
    def save(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        phone: str,
        email: str,
        counterparty_type: str,
        edrpou: str,
        counterparty_property: str,
        city_ref: str,
    ):
        return self._call_with_props(
            FirstName=first_name,
            MiddleName=middle_name,
            LastName=last_name,
            Phone=phone,
            Email=email,
            CounterpartyType=counterparty_type,
            EDRPOU=edrpou,
            CounterpartyProperty=counterparty_property,
            CityRef=city_ref,
        )

    @api_method("update")
    def update(
        self,
        ref: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        counterparty_type: str,
        counterparty_property: str,
        city_ref: str,
        phone: OptStr = None,
        email: OptStr = None,
    ):
        return self._call_with_props(
            Ref=ref,
            FirstName=first_name,
            MiddleName=middle_name,
            LastName=last_name,
            Phone=phone,
            Email=email,
            CounterpartyType=counterparty_type,
            CounterpartyProperty=counterparty_property,
            CityRef=city_ref,
        )

    @api_method("delete")
    def delete(self, ref: str):
        return self._call_with_props(Ref=ref)

    @api_method("getCounterpartyAddresses")
    def get_counterparty_addresses(
        self, ref: str, counterparty_property: OptStr = None
    ):
        return self._call_with_props(
            Ref=ref, CounterpartyProperty=counterparty_property
        )

    @api_method("getCounterpartyOptions")
    def get_counterparty_options(self, ref: str):
        return self._call_with_props(Ref=ref)

    @api_method("getCounterpartyContactPersons")
    def get_counterparty_contact_persons(self, ref: str, page: int = 1):
        return self._call_with_props(Ref=ref, Page=page)

    @api_method("getCounterparties")
    def get_counterparties(self, counterparty_property: str, page: int = 1):
        return self._call_with_props(
            CounterpartyProperty=counterparty_property, Page=page
        )
