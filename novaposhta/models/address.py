"""Address model module."""

from .base import BaseModel, api_method

from ..types import OptStr, OptBool


class Address(BaseModel):
    """
    Address model class.
    """

    name = "Address"

    def __init__(self, client):
        super().__init__(client)

    @api_method("searchSettlements")
    def search_settlements(self, city_name: str, limit: int = 50, page: int = 1):
        """
        Search settlements by city name.

        :param city_name: city name.
        :param page: page number.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(CityName=city_name, Limit=limit, Page=page)

    @api_method("searchSettlementStreets")
    def search_settlement_streets(
        self, street_name: str, settlement_ref: str, limit: int = 50
    ):
        """
        Search settlement streets by street name.

        :param street_name: street name.
        :param settlement_ref: settlement reference.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(
            StreetName=street_name, SettlementRef=settlement_ref, Limit=limit
        )

    @api_method("save")
    def save(
        self,
        counterparty_ref: str,
        street_ref: str,
        building_number: str,
        flat: str,
        note: OptStr = None,
    ):
        """
        Save address.

        :param counterparty_ref: counterparty reference.
        :param street_ref: street reference.
        :param building_number: building number.
        :param flat: flat.
        :param note: note.
        :return: response dict.
        """
        return self._call_with_props(
            CounterpartyRef=counterparty_ref,
            StreetRef=street_ref,
            BuildingNumber=building_number,
            Flat=flat,
            Note=note,
        )

    @api_method("delete")
    def delete(self, ref: str):
        """
        Delete address.

        :param ref: address reference.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref)

    @api_method("update")
    def update(
        self,
        ref: str,
        street_ref: OptStr = None,
        building_number: OptStr = None,
        flat: OptStr = None,
        note: OptStr = None,
        counterparty_ref: OptStr = None,
    ):
        """
        Update address.

        :param ref: address reference.
        :param street_ref: street reference.
        :param building_number: building number.
        :param flat: flat.
        :param note: note.
        :param counterparty_ref: counterparty reference.
        :return: response dict.
        """
        return self._call_with_props(
            Ref=ref,
            StreetRef=street_ref,
            BuildingNumber=building_number,
            Flat=flat,
            Note=note,
            CounterpartyRef=counterparty_ref,
        )

    @api_method("getSettlements")
    def get_settlements(
        self,
        area_ref: OptStr = None,
        ref: OptStr = None,
        region_ref: OptStr = None,
        page: int = 1,
        warehouse: bool = True,
        find_by_string: OptStr = None,
        limit: int = 50,
    ):
        """
        Get settlements.

        :param area_ref: area reference.
        :param ref: settlement reference.
        :param region_ref: region reference.
        :param page: page number.
        :param warehouse: warehouse.
        :param find_by_string: find by string.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(
            AreaRef=area_ref,
            Ref=ref,
            RegionRef=region_ref,
            Page=page,
            Warehouse=int(warehouse),
            FindByString=find_by_string,
            Limit=limit,
        )

    @api_method("getCities")
    def get_cities(
        self,
        ref: OptStr = None,
        find_by_string: OptStr = None,
        page: int = 1,
        limit: int = 50,
    ):
        """
        Get cities.

        :param ref: city reference.
        :param page: page number.
        :param limit: limit of items per page.
        :param find_by_string: find by string.
        :return: response dict.
        """
        return self._call_with_props(
            Ref=ref, Page=page, FindByString=find_by_string, Limit=limit
        )

    @api_method("getAreas")
    def get_areas(self):
        """
        Get areas.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getWarehouses")
    def get_warehouses(
        self,
        bicycle_parking: OptBool = None,
        post_finance: OptBool = None,
        city_name: OptStr = None,
        city_ref: OptStr = None,
        page: int = 1,
        find_by_string: OptStr = None,
        limit: int = 50,
        settlement_ref: OptStr = None,
        type_of_warehouse_ref: OptStr = None,
        warehouse_id: OptStr = None,
    ):
        """
        Get warehouses.

        :param bicycle_parking: bicycle parking presence.
        :param post_finance: post finance presence.
        :param city_name: city name.
        :param city_ref: city reference.
        :param page: page number.
        :param find_by_string: find by string.
        :param limit: limit of items per page.
        :param settlement_ref: settlement reference.
        :param type_of_warehouse_ref: type of warehouse reference.
        :param warehouse_id: warehouse id.
        :return: response dict.
        """
        if bicycle_parking is not None:
            bicycle_parking = int(bicycle_parking)
        if post_finance is not None:
            post_finance = int(post_finance)
        return self._call_with_props(
            BicycleParking=bicycle_parking,
            PostFinance=post_finance,
            CityName=city_name,
            CityRef=city_ref,
            Page=page,
            FindByString=find_by_string,
            Limit=limit,
            SettlementRef=settlement_ref,
            TypeOfWarehouseRef=type_of_warehouse_ref,
            WarehouseId=warehouse_id,
        )

    @api_method("getWarehouseTypes")
    def get_warehouse_types(self):
        """
        Get warehouse types.

        :return: response dict.
        """
        return self._call_with_props()

    @api_method("getStreet")
    def get_street(
        self, city_ref: str, find_by_string: str, page: int = 1, limit: int = 50
    ):
        """
        Get street.

        :param city_ref: city reference.
        :param find_by_string: find by string.
        :param page: page number.
        :param limit: limit of items per page.
        :return: response dict.
        """
        return self._call_with_props(
            CityRef=city_ref, FindByString=find_by_string, Page=page, Limit=limit
        )

    @api_method("getSettlementCountryRegion")
    def get_settlement_country_region(self, area_ref):
        """
        Get settlement country region.

        :param area_ref: area reference.
        :return: response dict.
        """
        return self._call_with_props(AreaRef=area_ref)

    @api_method("getSettlementAreas")
    def get_settlement_areas(self, ref):
        """
        Get settlement areas.

        :param ref: settlement reference.
        :return: response dict.
        """
        return self._call_with_props(Ref=ref)
