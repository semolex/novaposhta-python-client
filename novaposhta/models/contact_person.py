"""ContactPerson model module."""

from novaposhta.models.base import BaseModel, api_method


class ContactPerson(BaseModel):
    name = "ContactPerson"

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
        counterparty_ref: str,
    ):
        return self._call_with_props(
            FirstName=first_name,
            MiddleName=middle_name,
            LastName=last_name,
            Phone=phone,
            Email=email,
            CounterpartyRef=counterparty_ref,
        )

    @api_method("update")
    def update(
        self,
        ref: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        phone: str,
        email: str,
        counterparty_ref: str,
    ):
        return self._call_with_props(
            Ref=ref,
            FirstName=first_name,
            MiddleName=middle_name,
            LastName=last_name,
            Phone=phone,
            Email=email,
            CounterpartyRef=counterparty_ref,
        )

    @api_method("delete")
    def delete(self, ref: str):
        return self._call_with_props(Ref=ref)
