"""InternetDocument model module."""

from typing import List, Dict, Any, Optional

from novaposhta.models.base import BaseModel, api_method
from novaposhta.types import OptStr, StrOrNum, OptDictList, OptDict, OptInt, OptStrOrNum


class InternetDocument(BaseModel):
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
        cargo_details: OptDictList = None,
        cargo_description: OptStr = None,
    ):
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
        options_seat: Optional[List[Dict[str, StrOrNum]]] = None,
        red_box_barcode: OptStr = None,
        backward_delivery_data: Optional[List[Dict[str, Any]]] = None,
        recipient_address_note: OptStr = None,
    ):
        """ """

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
        return self._call_with_props(
            DateTimeFrom=date_time_from,
            DateTimeTo=date_time_to,
            Page=page,
            GetFullList=int(get_full_list),
            DateTime=date_time,
        )

    @api_method("delete")
    def delete(self, document_refs: str):
        return self._call_with_props(DocumentRefs=document_refs)

    @api_method("generateReport")
    def generate_report(self, document_refs: List[str], _type: str, date_time: str):
        return self._call_with_props(
            DocumentRefs=document_refs, Type=_type, DateTime=date_time
        )
