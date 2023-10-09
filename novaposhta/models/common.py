"""Common model module."""

from novaposhta.models.base import BaseModel, api_method

from novaposhta.types import OptStr, OptInt


class Common(BaseModel):
    name = "Common"

    def __init__(self, client):
        super().__init__(client)

    @api_method("getTimeIntervals")
    def get_time_intervals(self, recipient_city_ref: str, datetime: OptStr = None):
        return self._call_with_props(
            RecipientCityRef=recipient_city_ref, DateTime=datetime
        )

    @api_method("getCargoTypes")
    def get_cargo_types(self):
        return self._call_with_props()

    @api_method("getBackwardDeliveryCargoTypes")
    def get_backward_delivery_cargo_types(self):
        return self._call_with_props()

    @api_method("getPalletsList")
    def get_pallets_list(self):
        return self._call_with_props()

    @api_method("getTypesOfPayersForRedelivery")
    def get_types_of_payers_for_redelivery(self):
        return self._call_with_props()

    @api_method("getPackList")
    def get_pack_list(
        self,
        length: OptInt = None,
        width: OptInt = None,
        height: OptInt = None,
        volumetric_weight: OptInt = None,
        type_of_packing: OptStr = None,
    ):
        return self._call_with_props(
            Length=length,
            Width=width,
            Height=height,
            VolumetricWeight=volumetric_weight,
            TypeOfPacking=type_of_packing,
        )

    @api_method("getTiresWheelsList")
    def get_tires_wheels_list(self):
        return self._call_with_props()

    @api_method("getCargoDescriptionList")
    def get_cargo_description_list(self, find_by_string: OptStr = None, page: int = 1):
        return self._call_with_props(FindByString=find_by_string, Page=page)

    @api_method("getMessageCodeText")
    def get_message_code_text(self):
        return self._call_with_props()

    @api_method("getServiceTypes")
    def get_service_types(self):
        return self._call_with_props()

    @api_method("getOwnershipFormsList")
    def get_ownership_forms_list(self):
        return self._call_with_props()
