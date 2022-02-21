from app.api.v2.metadata.card_loan.repository import CardConfigsRepository
from app.api.v2.metadata.common.repository import CommonConfigsRepository
from app.api.v2.metadata.normal_loan.repository import NormalConfigsRepository
from app.utils.constant.configs import (
    CONST_AUTHENTICATION_QUESTION, CONST_BUSINESS_TYPE, CONST_CAREERS,
    CONST_DISTRICTS, CONST_DOCUMENT_TYPE, CONST_GIFT_SELECTION,
    CONST_LOAN_PRODUCT, CONST_PARTNER, CONST_PARTNER_PRODUCT,
    CONST_PERSONAL_REP, CONST_POLICY_DETAIL, CONST_TYPE_CARD_USE,
    CONST_TYPE_EXCEPTION, CONST_VEHICLE_DETAIL, CONST_WARDS, Configs
)
from app.utils.constant.source_income import BUSINESS_TYPE_SH_FOREOWNED

func_config_switcher = {
    Configs.countries: CommonConfigsRepository().get_countries,
    Configs.provinces: CommonConfigsRepository().get_provinces,
    Configs.districts: CommonConfigsRepository().get_districts,
    Configs.wards: CommonConfigsRepository().get_wards,
    Configs.loan_product: CommonConfigsRepository().get_loan_product,
    Configs.partner: CommonConfigsRepository().get_partner,
    Configs.partner_product: CommonConfigsRepository().get_partner_product,
    Configs.personal_rep: CommonConfigsRepository().get_personal_rep,
    Configs.collateral_type: CommonConfigsRepository().get_collateral_type,
    Configs.type_real_estate: CommonConfigsRepository().get_type_real_estate,
    Configs.type_exception: CommonConfigsRepository().get_type_exception,
    Configs.policy_detail: CommonConfigsRepository().get_policy_detail,
    Configs.score_rank_detail: CommonConfigsRepository().get_score_rank_detail,
    Configs.property_type: CommonConfigsRepository().get_property_type,
    Configs.vehicle_type: CommonConfigsRepository().get_vehicle_type,
    Configs.vehicle_detail: CommonConfigsRepository().get_vehicle_detail,
    Configs.list_legal_document: CommonConfigsRepository().get_list_legal_document,
    Configs.issuer: CommonConfigsRepository().get_issuer,
    Configs.country_manufacture: CommonConfigsRepository().get_country_manufacture,
    Configs.other_country_manufacture: CommonConfigsRepository().get_other_country_manufacture,
    Configs.price_appraisal: CommonConfigsRepository().get_price_appraisal,
    Configs.independent_valuation: CommonConfigsRepository().get_independent_valuation,
    Configs.credit_institution: NormalConfigsRepository().get_credit_institution,
    Configs.currency_type: NormalConfigsRepository().get_currency_type,
    Configs.schedule: NormalConfigsRepository().get_schedule,
    Configs.document_type: NormalConfigsRepository().get_document_type,
    Configs.authen_question: CardConfigsRepository().get_authen_question,
    Configs.type_card_use: CardConfigsRepository().get_type_card_use,
    Configs.gift_selection: CardConfigsRepository().get_gift_selection,
}


# -----------------------------------------------------------------------------------------------------
# HANDLE RESPONSE
async def response_districts(raws, *arg, **kwargs):
    province_code = kwargs.get(CONST_DISTRICTS)
    if not province_code:
        return raws
    if isinstance(province_code, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
            if raw["province_code"] == province_code
        ]
        data = sorted(data, key=lambda x: x['name'])
    elif isinstance(province_code, list):
        data = dict()
        for code in province_code:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
                if raw["province_code"] == str(code)
            ]
            data[code] = sorted(data[code], key=lambda x: x['name'])
    return data


async def response_wards(raws, *arg, **kwargs):
    district_code = kwargs.get(CONST_WARDS)
    if isinstance(district_code, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
            if raw["district_code"] == district_code
        ]
        data = sorted(data, key=lambda x: x['name'])
    elif isinstance(district_code, list):
        data = dict()
        for code in district_code:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
                if raw["district_code"] == str(code)
            ]
            data[code] = sorted(data[code], key=lambda x: x['name'])
    return data


async def response_loan_product(raws, *arg, **kwargs):
    loan_type = kwargs.get(CONST_LOAN_PRODUCT)
    if not loan_type:
        return raws

    if isinstance(loan_type, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name'], "parent_id": raw["parent_id"], "financial_analysis_flag": raw["financial_analysis_flag"]} for raw in raws
            if raw["product_loan_group_id"] == loan_type
        ]
    elif isinstance(loan_type, list):
        data = dict()
        for code in loan_type:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name'], "parent_id": raw["parent_id"], "financial_analysis_flag": raw["financial_analysis_flag"]} for raw in raws
                if raw["product_loan_group_id"] == code
            ]

    return data


async def response_partner(raws, *arg, **kwargs):
    loan_product_id = kwargs.get(CONST_PARTNER)
    if not loan_product_id:
        return raws
    if isinstance(loan_product_id, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
            if raw["loan_product_id"] == loan_product_id
        ]
    elif isinstance(loan_product_id, list):
        data = dict()
        for code in loan_product_id:
            data[data] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
                if raw["loan_product_id"] == code
            ]

    return data


async def response_partner_product(raws, *arg, **kwargs):
    partner_id = kwargs.get(CONST_PARTNER_PRODUCT)
    if not partner_id:
        return raws
    if isinstance(partner_id, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
            if raw["partner_id"] == partner_id
        ]
    elif isinstance(partner_id, list):
        data = dict()
        for code in partner_id:
            data[data] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']} for raw in raws
                if raw["partner_id"] == code
            ]

    return data


async def response_personal_rep(raws, *arg, **kwargs):
    type_loan = kwargs.get(CONST_PERSONAL_REP)
    if isinstance(type_loan, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
            for raw in raws if raw["loan_category_id"] == type_loan
        ]
    elif isinstance(type_loan, list):
        data = dict()
        for code in type_loan:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
                for raw in raws if raw["loan_category_id"] == code
            ]

    return data


async def response_type_business(raws, *arg, **kwargs):
    business_type_sh = kwargs.get(CONST_BUSINESS_TYPE)
    if isinstance(business_type_sh, str):
        if business_type_sh == BUSINESS_TYPE_SH_FOREOWNED:
            data = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
                for raw in raws if business_type_sh in raw["id"]
            ]
        else:
            data = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
                for raw in raws if business_type_sh not in raw["id"]
            ]
    elif isinstance(business_type_sh, list):
        data = dict()
        for code in business_type_sh:
            if business_type_sh == BUSINESS_TYPE_SH_FOREOWNED:
                data[code] = [
                    {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
                    for raw in raws if business_type_sh in raw["id"]
                ]
            else:
                data[code] = [
                    {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
                    for raw in raws if business_type_sh not in raw["id"]
                ]
    else:
        return raws

    return data


async def response_type_exception(raws, *arg, **kwargs):
    loan_product = kwargs.get(CONST_TYPE_EXCEPTION)

    if isinstance(loan_product, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name'], "description":raw["description"]}
            for raw in raws if raw["loan_product_id"] == loan_product
        ]
    elif isinstance(loan_product, list):
        data = dict()
        for code in loan_product:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name'], "description":raw["description"]}
                for raw in raws if raw["loan_product_id"] == code
            ]

    return data


async def response_policy_detail(raws, *arg, **kwargs):
    policy_detail = kwargs.get(CONST_POLICY_DETAIL)
    if isinstance(policy_detail, dict):

        policy_group_id = policy_detail.get(CONST_TYPE_EXCEPTION)
        loan_product_id = policy_detail.get(CONST_LOAN_PRODUCT)

        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name'], "description":raw["description"]}
            for raw in raws if raw["loan_product_id"] == loan_product_id and str(raw["policy_group_id"]) == policy_group_id
        ]
    else:
        return raws

    return data


# ----------------------------------------------------------------------------------------------------------------
# Response for credit normal loan
async def response_careers(raws, *arg, **kwargs):

    raws = sorted(raws, key=lambda x: x['code'])
    data = [
        {"id": raw['id'], "code": raw['code'], "name": raw['name'], "is_default":raw["is_default"]}
        for raw in raws
    ]

    return data


async def response_document_type(raws, *arg, **kwargs):
    document_group_type = kwargs.get(CONST_DOCUMENT_TYPE)
    data = [
        {"id": raw['id'], "code": raw['code'], "name": raw['name'], "parent_id":raw["parent_id"]}
        for raw in raws if raw["document_group_type"] == document_group_type
    ]

    return data


# ----------------------------------------------------------------------------------------------------------------
# Response for credit card loan
async def response_authen_question(raws, *arg, **kwargs):
    loan_product = kwargs.get(CONST_AUTHENTICATION_QUESTION)
    if not loan_product:
        return raws
    if isinstance(loan_product, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name']}
            for raw in raws if raw["loan_product_id"] == loan_product
        ]
    elif isinstance(loan_product, list):
        data = dict()
        for code in loan_product:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']}
                for raw in raws if raw["loan_product_id"] == code
            ]

    return data


async def response_type_card_use(raws, *arg, **kwargs):
    loan_product = kwargs.get(CONST_TYPE_CARD_USE)
    if not loan_product:
        return raws
    if isinstance(loan_product, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name'], "group_id": raw['group_id'], "product_card_id": raw['product_card_id']}
            for raw in raws if raw["loan_product_id"] == loan_product
        ]
    elif isinstance(loan_product, list):
        data = dict()
        for code in loan_product:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']}
                for raw in raws if raw["loan_product_id"] == code
            ]

    return data


async def response_gift_selection(raws, *arg, **kwargs):
    loan_product = kwargs.get(CONST_GIFT_SELECTION)
    if not loan_product:
        return raws
    if isinstance(loan_product, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name']}
            for raw in raws if raw["loan_product_id"] == loan_product
        ]
    elif isinstance(loan_product, list):
        data = dict()
        for code in loan_product:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name']}
                for raw in raws if raw["loan_product_id"] == code
            ]

    return data


async def response_vehicle_detail(raws, *arg, **kwargs):
    vehicle_type = kwargs.get(CONST_VEHICLE_DETAIL)
    if not vehicle_type:
        return raws
    if isinstance(vehicle_type, str):
        data = [
            {"id": raw['id'], "code": raw['code'], "name": raw['name'], "other_value_flag": raw['other_value_flag']}
            for raw in raws if raw["trans_type_id"] == vehicle_type
        ]
    elif isinstance(vehicle_type, list):
        data = dict()
        for code in vehicle_type:
            data[code] = [
                {"id": raw['id'], "code": raw['code'], "name": raw['name'], "other_value_flag": raw['other_value_flag']}
                for raw in raws if raw["trans_type_id"] == code
            ]

    return data


# -----------------------------------------------------------------------------------------------------
# FUNCTION SWITCHER RESPONSE
func_response_switcher = {
    CONST_DISTRICTS: response_districts,
    CONST_WARDS: response_wards,
    CONST_LOAN_PRODUCT: response_loan_product,
    CONST_PARTNER: response_partner,
    CONST_PARTNER_PRODUCT: response_partner_product,
    CONST_PERSONAL_REP: response_personal_rep,
    CONST_BUSINESS_TYPE: response_type_business,
    CONST_TYPE_EXCEPTION: response_type_exception,
    CONST_POLICY_DETAIL: response_policy_detail,
    CONST_CAREERS: response_careers,
    CONST_DOCUMENT_TYPE: response_document_type,
    CONST_AUTHENTICATION_QUESTION: response_authen_question,
    CONST_TYPE_CARD_USE: response_type_card_use,
    CONST_GIFT_SELECTION: response_gift_selection,
    CONST_VEHICLE_DETAIL: response_vehicle_detail
}
