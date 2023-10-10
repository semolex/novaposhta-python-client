"""Counterparty model module."""

from .base import BaseModel, api_method

from ..types import OptStr


class Counterparty(BaseModel):
    """
    Counterparty model class.
    """

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
        """
        Save counterparty.

        :param first_name: first name.
        :param middle_name: middle name.
        :param last_name: last name.
        :param phone: phone.
        :param email: email.
        :param counterparty_type: counterparty type.
        :param edrpou: EDRPOU.
        :param counterparty_property: counterparty property.
        :param city_ref: city reference.
        :return: response dict.
        """
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
        """
        Update counterparty.

        :param ref: counterparty reference.
        :param first_name: first name.
        :param middle_name: middle name.
        :param last_name: last name.
        :param phone: phone.
        :param email: email.
        :param counterparty_type: counterparty type.
        :param counterparty_property: counterparty property.
        :param city_ref: city reference.
        :return: response dict.
        """
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
        """
        Delete counterparty.

        :param ref: counterparty reference.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref)

    @api_method("getCounterpartyAddresses")
    def get_counterparty_addresses(
        self, ref: str, counterparty_property: OptStr = None
    ):
        """
        Get counterparty addresses.

        :param ref: counterparty reference.
        :param counterparty_property: counterparty property.
        :return: response dict.
        """
        return self._call_with_props(
            Ref=ref, CounterpartyProperty=counterparty_property
        )

    @api_method("getCounterpartyOptions")
    def get_counterparty_options(self, ref: str):
        """
        Get counterparty options.

        :param ref: counterparty reference.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref)

    @api_method("getCounterpartyContactPersons")
    def get_counterparty_contact_persons(self, ref: str, page: int = 1):
        """
        Get counterparty contact persons.

        :param ref: counterparty reference.
        :param page: page number.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref, Page=page)

    @api_method("getCounterparties")
    def get_counterparties(self, counterparty_property: str, page: int = 1):
        """
        Get counterparties.

        :param counterparty_property: counterparty property.
        :param page: page number.
        :return: response dict.
        """
        return self._call_with_props(
            CounterpartyProperty=counterparty_property, Page=page
        )
