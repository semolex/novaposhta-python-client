"""AdditionalService model module."""

from .base import BaseModel, api_method

from ..types import OptStr, StrOrNum


class AdditionalService(BaseModel):
    """
    AdditionalService model class.
    """

    name = "AdditionalService"

    def __init__(self, client):
        super().__init__(client)

    @api_method("CheckPossibilityCreateReturn")
    def check_possibility_create_return(self, number: StrOrNum):
        """
        Check possibility create return.

        :param number: Number of document.
        :return: response dict.
        """
        return self._call_with_props(Number=number)

    @api_method("getReturnReasons")
    def get_return_reasons(self):
        """
        Get return reasons.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getReturnReasonsSubtypes")
    def get_return_reasons_subtypes(self, reason_ref: str):
        """
        Get return reasons subtypes.

        :param reason_ref: Reason reference.
        :return: response dict.
        """
        return self._call_with_props(ReasonRef=reason_ref)

    @api_method("save")
    def save(
        self,
        int_doc_number: str,
        payment_method: str,
        note: str,
        order_type: str = "orderCargoReturn",
        reason: OptStr = None,
        sub_type_reason: OptStr = None,
        return_address_ref: OptStr = None,
        sender_contact_name: OptStr = None,
        sender_phone: OptStr = None,
        recipient: OptStr = None,
        recipient_contact_name: OptStr = None,
        recipient_phone: OptStr = None,
        payer_type: OptStr = None,
        customer: OptStr = None,
        service_type: OptStr = None,
        recipient_settlement: OptStr = None,
        recipient_settlement_street: OptStr = None,
        building_number: OptStr = None,
        note_address_recipient: OptStr = None,
        recipient_warehouse: OptStr = None,
    ):
        """
        Create return order.

        :param int_doc_number: document number.
        :param payment_method: payment method.
        :param note: custom description.
        :param order_type: order type.
        :param reason: reason for return.
        :param sub_type_reason: subtype of the reason for return.
        :param return_address_ref: reference to the return address.
        :param sender_contact_name: contact person for the sender.
        :param sender_phone: phone number of the sender.
        :param recipient: identifier of the recipient counterparty.
        :param recipient_contact_name: full name of the recipient contact person.
        :param recipient_phone: phone number of the recipient.
        :param payer_type: type of payer.
        :param customer: customer redirecting the order.
        :param service_type: type of service.
        :param recipient_settlement: identifier of the recipient's settlement.
        :param recipient_settlement_street: street identifier in the recipient's settlement.
        :param building_number: building number for redirection.
        :param note_address_recipient: comment on the recipient's address.
        :param recipient_warehouse: identifier of the recipient's warehouse.
        :return: response dict.
        """
        return self._call_with_props(
            IntDocNumber=int_doc_number,
            PaymentMethod=payment_method,
            Reason=reason,
            SubtypeReason=sub_type_reason,
            OrderType=order_type,
            ReturnAddressRef=return_address_ref,
            Note=note,
            SenderContactName=sender_contact_name,
            SenderPhone=sender_phone,
            Recipient=recipient,
            RecipientContactName=recipient_contact_name,
            RecipientPhone=recipient_phone,
            PayerType=payer_type,
            Customer=customer,
            ServiceType=service_type,
            RecipientSettlement=recipient_settlement,
            RecipientSettlementStreet=recipient_settlement_street,
            BuildingNumber=building_number,
            NoteAddressRecipient=note_address_recipient,
            RecipientWarehouse=recipient_warehouse,
        )

    @api_method("getReturnOrdersList")
    def get_return_orders_list(
        self,
        number: OptStr = None,
        ref: OptStr = None,
        begin_date: OptStr = None,
        end_date: OptStr = None,
        page: int = 1,
        limit: int = 50,
    ):
        """
        Get return orders list.

        :param number: document number.
        :param ref: document reference.
        :param begin_date: begin date.
        :param end_date: end date.
        :param page: page number.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(
            Number=number,
            Ref=ref,
            BeginDate=begin_date,
            EndDate=end_date,
            Page=page,
            Limit=limit,
        )

    @api_method("delete")
    def delete(self, ref: str):
        """
        Delete return order.

        :param ref: document reference.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref)

    @api_method("CheckPossibilityChangeEW")
    def check_possibility_change_ew(self, int_doc_number: StrOrNum):
        """
        Check possibility to change data.

        :param int_doc_number: document number.
        :return: response dict.
        """
        return self._call_with_props(IntDocNumber=int_doc_number)

    @api_method("getChangeEWOrdersList")
    def get_change_ew_orders_list(
        self,
        begin_date: str,
        end_date: str,
        number: OptStr = None,
        ref: OptStr = None,
        page: int = 1,
        limit: int = 50,
    ):
        """
        Get change data orders list.

        :param begin_date: begin date.
        :param end_date: end date.
        :param number: document number.
        :param ref: document reference.
        :param page: page number.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(
            Number=number,
            Ref=ref,
            BeginDate=begin_date,
            EndDate=end_date,
            Page=page,
            Limit=limit,
        )

    @api_method("checkPossibilityForRedirecting")
    def check_possibility_for_redirecting(self, number: StrOrNum):
        """
        Check possibility for redirecting.

        :param number: document number.
        :return: response dict.
        """
        return self._call_with_props(Number=number)

    @api_method("getRedirectionOrdersList")
    def get_redirection_orders_list(
        self,
        number: OptStr = None,
        ref: OptStr = None,
        begin_date: OptStr = None,
        end_date: OptStr = None,
        page: int = 1,
        limit: int = 50,
    ):
        """
        Get redirection orders list.

        :param number: document number.
        :param ref: document reference.
        :param begin_date: begin date.
        :param end_date: end date.
        :param page: page number.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(
            Number=number,
            Ref=ref,
            BeginDate=begin_date,
            EndDate=end_date,
            Page=page,
            Limit=limit,
        )
