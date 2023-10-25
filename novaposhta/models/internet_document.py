"""InternetDocument model module."""

from typing import List

from .base import BaseModel, api_method
from ..types import (
    OptStr,
    StrOrNum,
    OptListOfDicts,
    OptDict,
    OptInt,
    OptStrOrNum,
)


class InternetDocument(BaseModel):
    """
    InternetDocument model class.
    """

    name = "InternetDocument"

    def __init__(self, client):
        super().__init__(client)

    @api_method("getDocumentPrice")
    def get_document_price(
        self,
        city_sender: str,
        city_recipient: str,
        weight: StrOrNum,
        service_type: str,
        cost: StrOrNum,
        cargo_type: str,
        seats_amount: int,
        redelivery_calculate: OptDict = None,
        pack_count: OptStr = None,
        pack_ref: OptStr = None,
        amount: OptStr = None,
        cargo_details: OptListOfDicts = None,
        cargo_description: OptStr = None,
    ):
        """
        Get document (delivery) price.

        :param city_sender: city sender.
        :param city_recipient: city recipient.
        :param weight: weight.
        :param service_type: service type.
        :param cost: cost.
        :param cargo_type: cargo type.
        :param seats_amount: seats amount.
        :param redelivery_calculate: redelivery calculate.
        :param pack_count: pack count.
        :param pack_ref: pack reference.
        :param amount: amount.
        :param cargo_details: cargo details.
        :param cargo_description: cargo description.
        :return: response dict.
        """
        return self._call_with_props(
            CitySender=city_sender,
            CityRecipient=city_recipient,
            Weight=weight,
            ServiceType=service_type,
            Cost=cost,
            CargoType=cargo_type,
            SeatsAmount=seats_amount,
            RedeliveryCalculate=redelivery_calculate,
            PackCount=pack_count,
            PackRef=pack_ref,
            Amount=amount,
            CargoDetails=cargo_details,
            CargoDescription=cargo_description,
        )

    @api_method("getDocumentDeliveryDate")
    def get_document_delivery_date(
        self,
        city_sender: str,
        city_recipient: str,
        service_type: str,
        date_time: OptStr = None,
    ):
        """
        Get document (delivery) date.

        :param city_sender: city sender.
        :param city_recipient: city recipient.
        :param service_type: service type.
        :param date_time: date and time.
        :return: response dict.
        """
        return self._call_with_props(
            CitySender=city_sender,
            CityRecipient=city_recipient,
            ServiceType=service_type,
            DateTime=date_time,
        )

    @api_method("save")
    def save(
        self,
        payer_type: OptStr = None,
        payment_method: OptStr = None,
        date_time: OptStr = None,
        cargo_type: OptStr = None,
        weight: OptStrOrNum = None,
        service_type: OptStr = None,
        seats_amount: OptInt = None,
        description: OptStrOrNum = None,
        cost: OptStrOrNum = None,
        city_sender: OptStr = None,
        sender: OptStr = None,
        sender_address: OptStr = None,
        contact_sender: OptStr = None,
        senders_phone: OptStr = None,
        recipients_phone: OptStr = None,
        city_recipient: OptStr = None,
        recipient: OptStr = None,
        recipient_address: OptStr = None,
        contact_recipient: OptStr = None,
        new_address: OptStr = None,
        recipient_city_name: OptStr = None,
        recipient_area: OptStr = None,
        recipient_area_regions: OptStr = None,
        recipient_address_name: OptStr = None,
        recipient_house: OptStr = None,
        recipient_flat: OptStr = None,
        recipient_name: OptStr = None,
        recipient_type: OptStr = None,
        settlement_type: OptStr = None,
        ownership_form: OptStr = None,
        recipient_contact_name: OptStr = None,
        edrpou: OptStr = None,
        sender_warehouse_index: OptStr = None,
        recipient_warehouse_index: OptStr = None,
        volume_general: OptStrOrNum = None,
        options_seat: OptListOfDicts = None,
        red_box_barcode: OptStr = None,
        backward_delivery_data: OptListOfDicts = None,
        recipient_address_note: OptStr = None,
    ):
        """
        Create document (delivery).

        :param payer_type: payer type.
        :param payment_method: payment method.
        :param date_time: date and time.
        :param cargo_type: cargo type.
        :param weight: weight.
        :param service_type: service type.
        :param seats_amount: seats amount.
        :param description: description.
        :param cost: cost.
        :param city_sender: city sender.
        :param sender: sender.
        :param sender_address: sender address.
        :param contact_sender: contact sender.
        :param senders_phone: sender's phone.
        :param recipients_phone: recipient's phone.
        :param city_recipient: city recipient.
        :param recipient: recipient.
        :param recipient_address: recipient address.
        :param contact_recipient: contact recipient.
        :param new_address: new address.
        :param recipient_city_name: recipient city name.
        :param recipient_area: recipient area.
        :param recipient_area_regions: recipient area regions.
        :param recipient_address_name: recipient address name.
        :param recipient_house: recipient house.
        :param recipient_flat: recipient flat.
        :param recipient_name: recipient name.
        :param recipient_type: recipient type.
        :param settlement_type: settlement type.
        :param ownership_form: ownership form.
        :param recipient_contact_name: recipient contact name.
        :param edrpou: EDRPOU.
        :param sender_warehouse_index: sender warehouse index.
        :param recipient_warehouse_index: recipient warehouse index.
        :param volume_general: volume general.
        :param options_seat: options seat.
        :param red_box_barcode: red box barcode.
        :param backward_delivery_data: backward delivery data.
        :param recipient_address_note: recipient address note.
        :return: response dict.
        """

        return self._call_with_props(
            PayerType=payer_type,
            PaymentMethod=payment_method,
            DateTime=date_time,
            CargoType=cargo_type,
            Weight=weight,
            ServiceType=service_type,
            SeatsAmount=seats_amount,
            Description=description,
            Cost=cost,
            CitySender=city_sender,
            Sender=sender,
            SenderAddress=sender_address,
            ContactSender=contact_sender,
            SendersPhone=senders_phone,
            RecipientsPhone=recipients_phone,
            CityRecipient=city_recipient,
            Recipient=recipient,
            RecipientAddress=recipient_address,
            ContactRecipient=contact_recipient,
            NewAddress=new_address,
            RecipientCityName=recipient_city_name,
            RecipientArea=recipient_area,
            RecipientAreaRegions=recipient_area_regions,
            RecipientAddressName=recipient_address_name,
            RecipientHouse=recipient_house,
            RecipientFlat=recipient_flat,
            RecipientName=recipient_name,
            RecipientType=recipient_type,
            SettlementType=settlement_type,
            OwnershipForm=ownership_form,
            RecipientContactName=recipient_contact_name,
            EDRPOU=edrpou,
            SenderWarehouseIndex=sender_warehouse_index,
            RecipientWarehouseIndex=recipient_warehouse_index,
            VolumeGeneral=volume_general,
            OptionsSeat=options_seat,
            RedBoxBarcode=red_box_barcode,
            BackwardDeliveryData=backward_delivery_data,
            RecipientAddressNote=recipient_address_note,
        )

    @api_method("update")
    def update(
        self,
        ref: str,
        payer_type: str,
        payment_method: str,
        date_time: str,
        cargo_type: str,
        weight: StrOrNum,
        service_type: str,
        seats_amount: int,
        description: str,
        cost: StrOrNum,
        city_sender: str,
        sender: str,
        sender_address: str,
        contact_sender: str,
        senders_phone: str,
        city_recipient: str,
        recipient: str,
        recipient_address: str,
        contact_recipient: str,
        recipients_phone: str,
        volume_general: OptStrOrNum = None,
    ):
        """
        Update document (delivery).

        :param ref: reference.
        :param payer_type: payer type.
        :param payment_method: payment method.
        :param date_time: date and time.
        :param cargo_type: cargo type.
        :param weight: weight.
        :param service_type: service type.
        :param seats_amount: seats amount.
        :param description: description.
        :param cost: cost.
        :param city_sender: city sender.
        :param sender: sender.
        :param sender_address: sender address.
        :param contact_sender: contact sender.
        :param senders_phone: sender's phone.
        :param city_recipient: city recipient.
        :param recipient: recipient.
        :param recipient_address: recipient address.
        :param contact_recipient: contact recipient.
        :param recipients_phone: recipient's phone.
        :param volume_general: volume general.
        :return: response dict.
        """
        return self._call_with_props(
            Ref=ref,
            PayerType=payer_type,
            PaymentMethod=payment_method,
            DateTime=date_time,
            CargoType=cargo_type,
            Weight=weight,
            ServiceType=service_type,
            SeatsAmount=seats_amount,
            Description=description,
            Cost=cost,
            CitySender=city_sender,
            Sender=sender,
            SenderAddress=sender_address,
            ContactSender=contact_sender,
            SendersPhone=senders_phone,
            CityRecipient=city_recipient,
            Recipient=recipient,
            RecipientAddress=recipient_address,
            ContactRecipient=contact_recipient,
            RecipientsPhone=recipients_phone,
            VolumeGeneral=volume_general,
        )

    @api_method("getDocumentList")
    def get_document_list(
        self,
        date_time_from: str,
        date_time_to: str,
        page: int = 1,
        get_full_list: bool = True,
        date_time: OptStr = None,
    ):
        """
        Get document (delivery) list.

        :param date_time_from: date and time from.
        :param date_time_to: date and time to.
        :param page: page number.
        :param get_full_list: get full list.
        :param date_time: date and time.
        :return: response dict.
        """
        return self._call_with_props(
            DateTimeFrom=date_time_from,
            DateTimeTo=date_time_to,
            Page=page,
            GetFullList=int(get_full_list),
            DateTime=date_time,
        )

    @api_method("getIncomingDocumentsByPhone")
    def get_incoming_documents_by_phone(
        self,
        date_from: OptStr = None,
        date_to: OptStr = None,
        limit: OptInt = None,
    ):
        """
        Get incoming documents.

        :param date_from: filter date from.
        :param date_from: filter date to.
        :param limit: maximum number of records.
        :return: response dict.
        """
        return self._call_with_props(
            DateFrom=date_from,
            DateTo=date_to,
            Limit=limit,
        )

    @api_method("delete")
    def delete(self, document_refs: str):
        """
        Delete document (delivery).

        :param document_refs: document references.
        :return: response dict.
        """
        return self._call_with_props(DocumentRefs=document_refs)

    @api_method("generateReport")
    def generate_report(self, document_refs: List[str], _type: str, date_time: str):
        """
        Generate report.

        :param document_refs: document references.
        :param _type: type.
        :param date_time: date and time.
        :return: response dict.
        """
        return self._call_with_props(
            DocumentRefs=document_refs, Type=_type, DateTime=date_time
        )
