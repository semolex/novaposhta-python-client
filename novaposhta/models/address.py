"""Address model module."""

from novaposhta.models.base import BaseModel, api_method

from novaposhta.types import OptStr, OptBool


class Address(BaseModel):
    name = "Address"

    def __init__(self, client):
        super().__init__(client)

    @api_method("searchSettlements")
    def search_settlements(self, city_name: str, limit: int = 50, page: int = 1):
        return self._call_with_props(CityName=city_name, Limit=limit, Page=page)

    @api_method("searchSettlementStreets")
    def search_settlement_streets(
        self, street_name: str, settlement_ref: str, limit: int = 50
    ):
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
        return self._call_with_props(
            CounterpartyRef=counterparty_ref,
            StreetRef=street_ref,
            BuildingNumber=building_number,
            Flat=flat,
            Note=note,
        )

    @api_method("delete")
    def delete(self, ref: str):
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
        page: int = 1,
        find_by_string: OptStr = None,
        limit: int = 50,
    ):
        return self._call_with_props(
            Ref=ref, Page=page, FindByString=find_by_string, Limit=limit
        )

    @api_method("getAreas")
    def get_areas(self):
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
        return self._call_with_props()

    @api_method("getStreet")
    def get_street(
        self, city_ref: str, find_by_string: str, page: int = 1, limit: int = 50
    ):
        return self._call_with_props(
            CityRef=city_ref, FindByString=find_by_string, Page=page, Limit=limit
        )

    @api_method("getSettlementCountryRegion")
    def get_settlement_country_region(self, area_ref):
        return self._call_with_props(AreaRef=area_ref)

    @api_method("getSettlementAreas")
    def get_settlement_areas(self, ref):
        return self._call_with_props(Ref=ref)
