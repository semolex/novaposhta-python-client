"""Python client for Nova Poshta company's API. """

import requests


def _kwargs_to_props(**kwargs):
    """
    Receives `kwargs` and returns them as dict to give easier manipulation
    for different methods.

    :param kwargs: kwargs
    :return: kwargs dict
    """
    props = {k: v for k, v in kwargs.items() if v}
    return props


class NovaPoshtaApi:
    """
    Base class that wraps call to the Nova Poshta API.
    Prepares requests and builds proper resource location.
    All API models can be accessed as instance properties.
    Info about models can be found here:
    https://devcenter.novaposhta.ua/docs/services/
    """

    def __init__(self, api_key,
                 api_endpoint='https://api.novaposhta.ua/v2.0/json/'):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.print_uri = 'https://my.novaposhta.ua/orders/printMarkings/'

    def send(self, model_name, api_method, method_props):
        """
        Prepares query for run and perform calls to the Nova Poshta API.

        :param model_name: name of the API model to call it method.
        :param api_method: method of the API to call for passed model
        :param method_props: requests properties.
        :return: Response object.
        """
        data = {
            'apiKey': self.api_key,
            'modelName': model_name,
            'calledMethod': api_method,
            "methodProperties": method_props
        }
        response = requests.post(self.api_endpoint, json=data,
                                 headers={'Content-Type': 'application/json'})
        return response

    @property
    def address(self):
        """
        Gives access to the Address model of Nova Poshta API and it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/556d7ccaa0fe4f08e8f7ce43
        """
        return _Address(self, 'Address')

    @property
    def counterparty(self):
        """
        Gives access to the Counterparty model of Nova Poshta API and
        it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/557eb8c8a0fe4f02fc455b2d
        """
        return _Counterparty(self, 'Counterparty')

    @property
    def contact_person(self):
        """
        Gives access to the ContactPerson model of Nova Poshta API and
        it's methods.
        ContactPerson model is described in different docs chapters.
        """
        return _ContactPerson(self, 'ContactPerson')

    @property
    def scan_sheet(self):
        """
        Gives access to the ScanSheet model of Nova Poshta API and
        it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/55662bd3a0fe4f10086ec96e
        """
        return _ScanSheet(self, 'ScanSheet')

    @property
    def common(self):
        """
        Gives access to the Common model of Nova Poshta API and
        it's methods.
        API docs:
        https://devcenter.novaposhta.ua/docs/services/55702570a0fe4f0cf4fc53ed
        """
        return _Common(self, 'Common')

    @property
    def additional_service(self):
        """
        Gives access to the AdditionalService model of Nova Poshta API and
        it's methods.
        AdditionalService is described in different docs chapters.
        """
        return _AdditionalService(self, 'AdditionalService')

    @property
    def internet_document(self):
        """
        Gives access to the InternetDocument model of Nova Poshta API and
        it's methods.
        InternetDocument is described in different docs chapters.
        """
        return _InternetDocument(self, 'InternetDocument')


class Model:
    """
    Base class for model.
    Uses NovaPoshta client to perform calls to the API and passes required
    model name.
    """
    def __init__(self, client, model_name):
        self._client = client
        self.model_name = model_name

    def _call(self, api_method, props):
        """
        Wraps call to the API by using client. Automatically passes model name.

        :param api_method: name of the called method from API.
        :param props: payload to send to API.
        :return: Response object.
        """
        return self._client.send(self.model_name, api_method, props)


class WarehouseFilter:
    """
    Wraps properties for warehouse filtering to simplify manipulating methods
    that uses warehouse filter.
    """
    def __init__(self, type_of_warehouse_ref=None, post_finance=None,
                 bicycle_parking=None, pos_terminal=None, city_name=None,
                 city_ref=None):
        self.filter = _kwargs_to_props(TypeOfWarehouseRef=type_of_warehouse_ref,
                                       PostFinance=post_finance,
                                       BycycleParking=bicycle_parking,
                                       POSTerminal=pos_terminal,
                                       CityName=city_name, CityRef=city_ref)


class _ContactPerson(Model):
    """
    Implements ContactPerson model.
    """
    def update(self, counterparty_ref, ref, first_name, last_name,
               phone, middle_name=None):
        props = _kwargs_to_props(CounterpartyRef=counterparty_ref, Ref=ref,
                                 FirstName=first_name, LastName=last_name,
                                 MiddleName=middle_name, Phone=phone)
        return self._call('update', props)

    def save(self, counterparty_ref, first_name, last_name, phone,
             counterparty_type, counterparty_property,
             middle_name=None):
        props = _kwargs_to_props(CounterpartyRef=counterparty_ref,
                                 FirstName=first_name, LastName=last_name,
                                 Phone=phone, MiddleName=middle_name,
                                 CounterpartyType=counterparty_type,
                                 CounterpartyProperty=counterparty_property)
        return self._call('save', props)

    def delete(self, ref):
        props = _kwargs_to_props(Ref=ref)
        return self._call('delete', props)


class _Address(Model):
    """
    Implements Address model.
    """
    def search_settlements(self, city_name, limit):
        props = _kwargs_to_props(CityName=city_name, Limit=limit)
        return self._call('searchSettlements', props)

    def search_settlement_streets(self, street_name, settlement_ref, limit):
        props = _kwargs_to_props(StreetName=street_name,
                                 SettlementRef=settlement_ref, Limit=limit)
        return self._call('searchSettlementStreets', props)

    def update(self, counterparty_ref=None, ref=None, street_ref=None,
               building_number=None, flat=None, note=None):
        props = _kwargs_to_props(CounterpartyRef=counterparty_ref,
                                 Ref=ref,
                                 StreetRef=street_ref,
                                 BuildingNumber=building_number,
                                 Flat=flat,
                                 Note=note
                                 )
        return self._call('update', props)

    def save(self, counterparty_ref, street_ref,
             building_number, flat, note=None):
        props = _kwargs_to_props(CounterpartyRef=counterparty_ref,

                                 StreetRef=street_ref,
                                 BuildingNumber=building_number,
                                 Flat=flat,
                                 Note=note
                                 )
        return self._call('save', props)

    def get_areas(self):
        return self._call('getAreas', {})

    def get_cities(self, ref=None, page=None, find_by_string=None):
        props = _kwargs_to_props(Ref=ref, Page=page,
                                 FindByString=find_by_string)
        return self._call('getCities', props)

    def get_settlements(self, ref=None, region_ref=None, find_by_string=None,
                        warehouse=None, area_ref=None, page=None):
        props = _kwargs_to_props(Ref=ref, RegionRef=region_ref,
                                 FindByString=find_by_string,
                                 Warehouse=warehouse, Page=page,
                                 AreaRef=area_ref)
        return self._client.send('AddressGeneral', 'getSettlements', props)

    def get_warehouses(self, city_name=None, city_ref=None, page=None,
                       limit=None, language=None, filter_by=None):
        props = _kwargs_to_props(CityName=city_name, CityRef=city_ref,
                                 Page=page, Limit=limit, Language=language)
        if filter_by:
            if isinstance(filter_by, WarehouseFilter):
                filter_by = filter_by.filter
            props.update(filter_by)
        return self._call('getWarehouses', props)

    def get_warehouse_types(self):
        return self._call('getWarehouseTypes', {})

    def get_street(self, city_ref, find_by_string=None, page=None):
        props = _kwargs_to_props(CityRef=city_ref, FindByString=find_by_string,
                                 Page=page)
        return self._call('getStreet', props)

    def delete(self, ref):
        props = _kwargs_to_props(Ref=ref)
        return self._call('delete', props)


class _Counterparty(Model):
    """
    Implements Counterparty model.
    """
    def get_counterparty_addresses(self, ref, counterparty_props):
        props = _kwargs_to_props(Ref=ref,
                                 CounterpartyProperty=counterparty_props)
        return self._call('getCounterpartyAddresses', props)

    def get_counterparty_options(self, ref):
        props = _kwargs_to_props(Ref=ref)
        return self._call('getCounterpartyOptions', props)

    def get_counterparty_contact_person(self, ref, page=None):
        props = _kwargs_to_props(Ref=ref, Page=page)
        return self._call('getCounterpartyContactPersons', props)

    def get_counterparties(self, counterparty_property=None, page=None,
                           find_by_string=None):
        props = _kwargs_to_props(CounterpartyProperty=counterparty_property,
                                 Page=page, FindByString=find_by_string)
        return self._call('getCounterparties', props)

    def update(self, city_ref, ref, first_name, last_name,
               phone, counterparty_type, counterparty_property,
               middle_name=None, email=None):
        props = _kwargs_to_props(CityRef=city_ref, Ref=ref,
                                 FirstName=first_name, LastName=last_name,
                                 MiddleName=middle_name, Phone=phone,
                                 CounterpartyType=counterparty_type,
                                 CounterpartyProperty=counterparty_property,
                                 Email=email)
        return self._call('update', props)

    def save(self, city_ref,
             counterparty_type, counterparty_property, first_name=None,
             middle_name=None, email=None, ownership_form=None, phone=None,
             last_name=None, edrpou=None):
        props = _kwargs_to_props(CounterpartyRef=city_ref,
                                 FirstName=first_name, LastName=last_name,
                                 Phone=phone, MiddleName=middle_name,
                                 CounterpartyType=counterparty_type,
                                 CounterpartyProperty=counterparty_property,
                                 Email=email,
                                 OwnershipForm=ownership_form,
                                 EDRPOU=edrpou)
        return self._call('save', props)

    def delete(self, ref):
        props = _kwargs_to_props(Ref=ref)
        return self._call('delete', props)


class _ScanSheet(Model):
    """
    Implements ScanSheet model.
    """
    def insert_documents(self, document_refs, ref=None, date=None):
        if not isinstance(document_refs, list):
            document_refs = [document_refs]
        props = _kwargs_to_props(DocumentRefs=document_refs, Ref=ref, Date=date)
        return self._call('insertDocuments', props)

    def get_scan_sheet(self, ref, counterparty_ref=None):
        props = _kwargs_to_props(Ref=ref, CounterpartyRef=counterparty_ref)
        return self._call('getScanSheet', props)

    def get_scan_sheet_list(self):
        return self._call('getScanSheetList', {})

    def delete_scan_sheet(self, scan_sheet_refs):
        if not isinstance(scan_sheet_refs, list):
            scan_sheet_refs = [scan_sheet_refs]
        props = _kwargs_to_props(ScanSheetRefs=scan_sheet_refs)
        return self._call('deleteScanSheet', props)

    def remove_documents(self, document_refs, ref=None):
        if not isinstance(document_refs, list):
            document_refs = [document_refs]
        props = _kwargs_to_props(DocumentRefs=document_refs, Ref=ref)
        return self._call('removeDocuments', props)


class _Common(Model):
    """
    Implements Common model.
    """
    def get_time_intervals(self, recipient_city_ref, datetime=None):
        props = _kwargs_to_props(RecipientCityRef=recipient_city_ref,
                                 DateTime=datetime)
        return self._call('getTimeIntervals', props)

    def get_cargo_types(self):
        return self._call('getCargoTypes', {})

    def get_backward_delivery_cargo_types(self):
        return self._call('getBackwardDeliveryCargoTypes', {})

    def get_pallets_list(self):
        return self._call('getPalletsList', {})

    def get_types_of_payers(self):
        return self._call('getTypesOfPayers', {})

    def get_types_of_payers_for_redelivery(self):
        return self._call('getTypesOfPayersForRedelivery', {})

    def get_pack_list(self):
        return self._call('getPackList', {})

    def get_tires_wheels_list(self):
        return self._call('getTiresWheelsList', {})

    def get_cargo_description_list(self, find_by_string=None, page=None):
        props = _kwargs_to_props(FindByString=find_by_string, Page=page)
        return self._call('getCargoDescriptionList', props)

    def get_message_code_text(self):
        return self._call('getMessageCodeText', {})

    def get_service_types(self):
        return self._call('getServiceTypes', {})

    def get_types_of_counterparties(self):
        return self._call('getTypesOfCounterparties', {})

    def get_payment_forms(self):
        return self._call('getPaymentForms', {})

    def get_ownership_forms_list(self):
        return self._call('getOwnershipFormsList', {})


class _AdditionalService(Model):
    """
    Implements AdditionalService model.
    """
    def check_possibility_create_return(self, number=None):
        props = _kwargs_to_props(Number=number)
        return self._call('CheckPossibilityCreateReturn', props)

    def get_return_reasons(self):
        return self._call('getReturnReasons', {})

    def get_return_reasons_subtypes(self, reason_ref=None):
        props = _kwargs_to_props(ReasonRef=reason_ref)
        return self._call('getReturnReasonsSubtypes', props)

    def order_cargo_return(self, int_doc_number, payment_method, reason,
                           subtype_reason,
                           return_address_ref, note=None):
        props = _kwargs_to_props(IntDocNumber=int_doc_number,
                                 PaymentMethod=payment_method, Reason=reason,
                                 SubtypeReason=subtype_reason,
                                 ReturnAddressRef=return_address_ref,
                                 OrderType='orderCargoReturn', Note=note)
        return self._call('save', props)

    def get_return_order_list(self, number=None, ref=None, begin_date=None,
                              end_date=None, page=None, limit=None):
        props = _kwargs_to_props(Number=number, Ref=ref, BeginDate=begin_date,
                                 EndDate=end_date, Page=page, Limit=limit)
        return self._call('getReturnOrdersList', props)

    def delete(self, ref):
        props = _kwargs_to_props(Ref=ref)
        return self._call('delete', props)

    def check_possibility_change_ew(self, int_doc_number):
        props = _kwargs_to_props(IntDocNumber=int_doc_number)
        return self._call('CheckPossibilityChangeEW', props)

    def order_change_ew(self, int_doc_number, sender_contact_name=None,
                        sender_phone=None, recipient=None,
                        recipient_contact_name=None, recipient_phone=None,
                        payer_type=None, payment_method=None):
        props = _kwargs_to_props(IntDocNumber=int_doc_number,
                                 SenderContactName=sender_contact_name,
                                 SenderPhone=sender_phone, Recipient=recipient,
                                 RecipientContactName=recipient_contact_name,
                                 RecipientPhone=recipient_phone,
                                 PayerType=payer_type,
                                 PaymentMethod=payment_method,
                                 OrderType='orderChangeEW')
        return self._call('save', props)

    def get_change_ew_orders_list(self, number=None, ref=None, begin_date=None,
                                  end_date=None, page=None, limit=None):
        props = _kwargs_to_props(Number=number, Ref=ref, BeginDate=begin_date,
                                 EndDate=end_date, Page=page, Limit=limit)
        return self._call('getChangeEWOrdersList', props)

    def check_possibility_for_redirecting(self, number):
        props = _kwargs_to_props(Number=number)
        return self._client.send('AdditionalServiceGeneral',
                                'checkPossibilityForRedirecting', props)

    def order_redirecting(self, int_doc_number, customer,
                          recipient_settlement, recipient_settlement_street,
                          building_number, service_type, note_address_recipient,
                          recipient_warehouse, recipient,
                          recipient_contact_name, recipient_phone, payer_type,
                          payment_method, note):
        props = _kwargs_to_props(IntDocNumber=int_doc_number, Customer=customer,
                                 RecipientSettlement=recipient_settlement,
                                 RecipientSettlementStreet=recipient_settlement_street,
                                 BuildingNumber=building_number,
                                 NoteAddressRecipient=note_address_recipient,
                                 RecipientWarehouse=recipient_warehouse,
                                 Recipient=recipient,
                                 RecipientContactName=recipient_contact_name,
                                 RecipientPhone=recipient_phone,
                                 PayerType=payer_type,
                                 ServiceType=service_type,
                                 PaymentMethod=payment_method,
                                 Note=note,
                                 OrderType='orderRedirecting'
                                 )
        return self._client.send('AdditionalServiceGeneral', 'save',
                                 props)

    def delete_order_redirecting(self, ref):
        props = _kwargs_to_props(Ref=ref, OrderType='orderRedirecting')
        return self._client.send('AdditionalServiceGeneral',
                                'delete', props)

    def get_redirection_orders_list(self, number=None, ref=None,
                                    begin_date=None,
                                    end_date=None, page=None, limit=None):
        props = _kwargs_to_props(Number=number, Ref=ref, BeginDate=begin_date,
                                 EndDate=end_date, Page=page, Limit=limit)
        return self._client.send('AdditionalServiceGeneral',
                                'getRedirectionOrdersList', props)


class _InternetDocument(Model):
    """
    Implements InternetDocument model.
    """
    def get_document_list(self, datetime_from=None, datetime_to=None, page=None,
                          get_full_list=None, datetime=None,
                          redelivery_money=None, unassembled_cargo=None):
        props = _kwargs_to_props(DateTimeFrom=datetime_from,
                                 DateTimeTo=datetime_to, Page=page,
                                 GetFullList=get_full_list, DateTime=datetime,
                                 RedeliveryMoney=redelivery_money,
                                 UnassembledCargo=unassembled_cargo)
        return self._call('getDocumentList', props)

    def get_document_delivery_date(self, service_type, city_sender,
                                   city_recipient, datetime=None):
        props = _kwargs_to_props(ServiceType=service_type,
                                 CitySender=city_sender,
                                 CityRecipient=city_recipient,
                                 DateTime=datetime)
        return self._call('getDocumentDeliveryDate', props)

    def get_document_price(self, city_sender, city_recipient, weight,
                           service_type, cost, cargo_type, seats_amount,
                           pack_count=None,
                           pack_ref=None, amount=None, cargo_details=None,
                           redelivery_cargo_type=None):
        props = _kwargs_to_props(CitySender=city_sender,
                                 CityRecipient=city_recipient, Weight=weight,
                                 ServiceType=service_type, Cost=cost,
                                 CargoType=cargo_type, SeatsAmount=seats_amount,
                                 RedeliveryCalculate={
                                     'CargoType': redelivery_cargo_type,
                                     'Amount': amount},
                                 PackCalculate={'PackCount': pack_count,
                                                'PackRef': pack_ref},

                                 Amount=amount, CargoDetails=cargo_details)
        return self._call('getDocumentPrice', props)

    def update(self, ref, payer_type, payment_method, datetime, cargo_type,
               weight, service_type, description,
               cost, city_sender, sender, sender_address, contact_sender,
               senders_phone, city_recipient, recipient, recipient_address,
               contact_recipient, recipients_phone, seats_amount=None,
               volume_general=None):
        props = _kwargs_to_props(Ref=ref, PayerType=payer_type,
                                 PaymentMethod=payment_method,
                                 DateTime=datetime, CargoType=cargo_type,
                                 VolumeGeneral=volume_general, Weight=weight,
                                 ServiceType=service_type,
                                 SeatsAmount=seats_amount,
                                 Description=description, Cost=cost,
                                 CitySender=city_sender, Sender=sender,
                                 SenderAddress=sender_address,
                                 ContactSender=contact_sender,
                                 SendersPhone=senders_phone,
                                 CityRecipient=city_recipient,
                                 Recipient=recipient,
                                 RecipientAddress=recipient_address,
                                 ContactRecipient=contact_recipient,
                                 RecipientsPhone=recipients_phone)
        return self._call('update', props)

    def save(self, from_waybill=None, payer_type=None, payment_method=None,
             cargo_type=None,
             service_type=None, description=None,
             cost=None, city_sender=None, sender=None, sender_address=None,
             contact_sender=None,
             senders_phone=None,
             recipients_phone=None,
             recipient_name=None, recipient_type=None,
             datetime=None, settlement_type=None, seats_amount=None,
             volume_general=None, city_recipient=None, recipient=None,
             recipient_address=None, contact_recipient=None, new_address=None,
             recipient_city_name=None, recipient_address_name=None,
             recipient_area=None, recipient_area_regions=None,
             recipient_house=None, recipient_flat=None, options_seat=None,
             weight=None, backward_delivery_data=None, is_take_attorney=None,
             cargo_details=None):
        if from_waybill and isinstance(from_waybill, ExpressWaybill):
            props = from_waybill.body
        else:
            props = _kwargs_to_props(NewAddress=new_address,
                                     PayerType=payer_type,
                                     PaymentMethod=payment_method,
                                     CargoType=cargo_type,
                                     VolumeGeneral=volume_general,
                                     Weight=weight,
                                     ServiceType=service_type,
                                     SeatsAmount=seats_amount,
                                     Description=description, Cost=cost,
                                     CitySender=city_sender, Sender=sender,
                                     SenderAddress=sender_address,
                                     ContactSender=contact_sender,
                                     SendersPhone=senders_phone,
                                     RecipientCityName=recipient_city_name,
                                     RecipientArea=recipient_area,
                                     RecipientAreaRegions=recipient_area_regions,
                                     RecipientAddressName=recipient_address_name,
                                     RecipientHouse=recipient_house,
                                     RecipientsPhone=recipients_phone,
                                     RecipientFlat=recipient_flat,
                                     RecipientName=recipient_name,
                                     RecipientType=recipient_type,
                                     Datetime=datetime,
                                     Recipient=recipient,
                                     CityRecipient=city_recipient,
                                     SettlementType=settlement_type,
                                     RecipientAddress=recipient_address,
                                     ContactRecipient=contact_recipient,
                                     OptionsSeat=options_seat,
                                     BackwardDeliveryData=backward_delivery_data,
                                     IsTakeAttorney=is_take_attorney,
                                     CargoDetails=cargo_details)
        if options_seat and not isinstance(options_seat, list):
            raise ValueError('options_seat must be passed as list of values')
        return self._call('save', props)

    def get_status_documents(self, documents):
        if not isinstance(documents, list):
            documents = [documents]
        props = _kwargs_to_props(Documents=documents)
        return self._client.send('TrackingDocument', 'getStatusDocuments', props)

    def delete(self, document_refs):
        if not isinstance(document_refs, list):
            document_refs = [document_refs]
        props = _kwargs_to_props(DocumentRefs=document_refs)
        return self._call('delete', props)

    def generate_report(self, document_refs, doc_type, datetime=None):
        if not isinstance(document_refs, list):
            document_refs = [document_refs]
        props = _kwargs_to_props(DocumentRefs=document_refs, DateTime=datetime,
                                 Type=doc_type)
        return self._call('generateReport', props)

    def get_cards(self):
        return self._client.send('Payment', 'getCards', {})


class ExpressWaybill:
    """
    Wraps express waybill schema for easier manipulating in
    InternetDocument model.
    """
    def __init__(self,
                 payer_type, payment_method,
                 cargo_type,
                 service_type, description,
                 cost, city_sender, sender, sender_address, contact_sender,
                 senders_phone,
                 recipients_phone,
                 recipient_name=None, recipient_type=None,
                 datetime=None, settlement_type=None, seats_amount=None,
                 volume_general=None, city_recipient=None, recipient=None,
                 recipient_address=None, contact_recipient=None,
                 new_address=None,
                 recipient_city_name=None, recipient_address_name=None,
                 recipient_area=None, recipient_area_regions=None,
                 recipient_house=None, recipient_flat=None, options_seat=None,
                 weight=None, backward_delivery_data=None,
                 is_take_attorney=None, cargo_details=None):
        self.body = _kwargs_to_props(NewAddress=new_address,
                                     PayerType=payer_type,
                                     PaymentMethod=payment_method,
                                     CargoType=cargo_type,
                                     VolumeGeneral=volume_general,
                                     Weight=weight,
                                     ServiceType=service_type,
                                     SeatsAmount=seats_amount,
                                     Description=description, Cost=cost,
                                     CitySender=city_sender, Sender=sender,
                                     SenderAddress=sender_address,
                                     ContactSender=contact_sender,
                                     SendersPhone=senders_phone,
                                     RecipientCityName=recipient_city_name,
                                     RecipientArea=recipient_area,
                                     RecipientAreaRegions=recipient_area_regions,
                                     RecipientAddressName=recipient_address_name,
                                     RecipientHouse=recipient_house,
                                     RecipientsPhone=recipients_phone,
                                     RecipientFlat=recipient_flat,
                                     RecipientName=recipient_name,
                                     RecipientType=recipient_type,
                                     Datetime=datetime,
                                     Recipient=recipient,
                                     CityRecipient=city_recipient,
                                     SettlementType=settlement_type,
                                     RecipientAddress=recipient_address,
                                     ContactRecipient=contact_recipient,
                                     OptionsSeat=options_seat,
                                     BackwardDeliveryData=backward_delivery_data,
                                     IsTakeAttorney=is_take_attorney,
                                     CargoDetails=cargo_details
                                     )

