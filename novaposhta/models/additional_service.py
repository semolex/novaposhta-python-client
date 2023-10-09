"""AdditionalService model module."""

from novaposhta.models.base import BaseModel, api_method

from novaposhta.types import OptStr, StrOrNum


class AdditionalService(BaseModel):
    name = "AdditionalService"

    def __init__(self, client):
        super().__init__(client)

    @api_method("CheckPossibilityCreateReturn")
    def check_possibility_create_return(self, number: StrOrNum):
        return self._call_with_props(Number=number)

    @api_method("getReturnReasons")
    def get_return_reasons(self):
        return self._call_with_props()

    @api_method("getReturnReasonsSubtypes")
    def get_return_reasons_subtypes(self, reason_ref: str):
        return self._call_with_props(ReasonRef=reason_ref)

    @api_method("save")
    def save(
        self,
        int_doc_number: StrOrNum,
        payment_method: str,
        reason: str,
        sub_type_reason: str,
        return_address_ref: str,
        order_type: str = "orderCargoReturn",
        note: str = "",
    ):
        return self._call_with_props(
            IntDocNumber=int_doc_number,
            PaymentMethod=payment_method,
            Reason=reason,
            SubtypeReason=sub_type_reason,
            OrderType=order_type,
            ReturnAddressRef=return_address_ref,
            Note=note,
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
        return self._call_with_props(Ref=ref)

    @api_method("CheckPossibilityChangeEW")
    def check_possibility_change_ew(self, int_doc_number: StrOrNum):
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
        return self._call_with_props(
            Number=number,
            Ref=ref,
            BeginDate=begin_date,
            EndDate=end_date,
            Page=page,
            Limit=limit,
        )
