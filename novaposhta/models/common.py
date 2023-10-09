"""Common model module."""

from .base import BaseModel, api_method

from ..types import OptStr, OptInt


class Common(BaseModel):
    """
    Common model class.
    """

    name = "Common"

    def __init__(self, client):
        super().__init__(client)

    @api_method("getTimeIntervals")
    def get_time_intervals(self, recipient_city_ref: str, datetime: OptStr = None):
        """
        Get time intervals.

        :param recipient_city_ref: recipient city reference.
        :param datetime: date and time.
        :return: response dict.
        """
        return self._call_with_props(
            RecipientCityRef=recipient_city_ref, DateTime=datetime
        )

    @api_method("getCargoTypes")
    def get_cargo_types(self):
        """
        Get cargo types.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getBackwardDeliveryCargoTypes")
    def get_backward_delivery_cargo_types(self):
        """
        Get backward delivery cargo types.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getPalletsList")
    def get_pallets_list(self):
        """
        Get pallets list.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getTypesOfPayersForRedelivery")
    def get_types_of_payers_for_redelivery(self):
        """
        Get types of payers for redelivery.

        :return: response dict.
        """
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
        """
        Get pack list.

        :param length: length.
        :param width: width.
        :param height: height.
        :param volumetric_weight: volumetric weight.
        :param type_of_packing: type of packing.
        :return: response dict.
        """
        return self._call_with_props(
            Length=length,
            Width=width,
            Height=height,
            VolumetricWeight=volumetric_weight,
            TypeOfPacking=type_of_packing,
        )

    @api_method("getTiresWheelsList")
    def get_tires_wheels_list(self):
        """
        Get tires wheels list.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getCargoDescriptionList")
    def get_cargo_description_list(self, find_by_string: OptStr = None, page: int = 1):
        """
        Get cargo description list.

        :param find_by_string: find by string.
        :param page: page number.
        :return: response dict.
        """
        return self._call_with_props(FindByString=find_by_string, Page=page)

    @api_method("getMessageCodeText")
    def get_message_code_text(self):
        """
        Get message code text.
        """
        return self._call_with_props()

    @api_method("getServiceTypes")
    def get_service_types(self):
        """
        Get service types.
        """
        return self._call_with_props()

    @api_method("getOwnershipFormsList")
    def get_ownership_forms_list(self):
        """
        Get ownership forms list.
        """
        return self._call_with_props()
