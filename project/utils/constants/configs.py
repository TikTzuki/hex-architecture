from enum import Enum

from app.utils.constant.udtm import (
    CIC_CUS_SEGMENT, COLLATERAL_APARTMENT_LEGAL_STATUS,
    COLLATERAL_APARTMENT_TYPE, COLLATERAL_APARTMENT_VALUATION_LAND_USE_PURPOSE,
    COLLATERAL_BALANCE_TYPE, COLLATERAL_CARGO_STATUS,
    COLLATERAL_CERT_LAND_USE_FORM, COLLATERAL_CERT_LAND_USE_SOURCE,
    COLLATERAL_CONST_CERT_TYPE, COLLATERAL_LAND_ASSET_LEGAL,
    COLLATERAL_LAND_ASSET_TYPE,
    COLLATERAL_LAND_ASSET_VALUATION_LAND_USE_PURPOSE,
    COLLATERAL_LAND_CERT_TYPE, COLLATERAL_LANE_WIDTH, COLLATERAL_LOCATION_TYPE,
    COLLATERAL_MACHINE_STATUS, COLLATERAL_RIGHT_PROPERTY_STATUS,
    COLLATERAL_TRANS_STATUS, COLLATERAL_VALUATION_PURPOSE, UDTM_ABLE_PAY_LABEL,
    UDTM_ACCEPT_CREDIT_LABEL, UDTM_ACCEPT_FLAG, UDTM_ACCEPT_STATUS,
    UDTM_ADDRESS_TYPE, UDTM_ASSET_RENT_TYPE, UDTM_AVERAGE_INCOME,
    UDTM_BUSINESS_LICENCE_TYPE, UDTM_BUSINESS_REPRESENTATIVE,
    UDTM_BUSINESS_TYPE, UDTM_BUSINESS_TYPE_SH, UDTM_CARD_DELIVERY_METHOD,
    UDTM_CAREER, UDTM_CIF_ID_TYPE, UDTM_COLLATERAL_OWNER_TYPE,
    UDTM_CONTRACT_TERM, UDTM_CURRENT_CARD_GUARANTEE_FORM,
    UDTM_CUST_CLASSIFICATION, UDTM_CUSTOMER_NEED, UDTM_CUSTOMER_TYPE,
    UDTM_DEBT_CLASSIFICATION, UDTM_DISBURSEMENT, UDTM_EDUCATION,
    UDTM_FATCA_INFO, UDTM_FREQUENCE, UDTM_LENDING_METHOD,
    UDTM_LOAN_PURPOSE_CORE, UDTM_MARITAL_STATUS, UDTM_OWNER_PROPERTY,
    UDTM_PAYMENT, UDTM_PRODUCT_CATEGORY, UDTM_PRODUCT_LOAN_PURPOSE,
    UDTM_PUBLICATION_SPEED_TYPE, UDTM_QUESTION, UDTM_REAL_ESTATE_STATUS,
    UDTM_RELATIONSHIP, UDTM_REMARK, UDTM_RESIDENT_STATUS, UDTM_RISK_TYPE,
    UDTM_SCHEDULE_UNIT, UDTM_SEX, UDTM_USED_OTHER_CONTRACT_LABEL,
    UDTM_WORK_STATUS, VALUATION_UNIT_TYPE
)

CONST_COUNTRIES = "COUNTRIES"
CONST_PROVINCES = "PROVINCES"
CONST_DISTRICTS = "DISTRICTS"
CONST_WARDS = "WARDS"
CONST_LOAN_PRODUCT = "LOAN_PRODUCT"
CONST_PARTNER = "PARTNER"
CONST_PARTNER_PRODUCT = "PARTNER_PRODUCT"
CONST_COLLATERAL = "COLLATERAL"
CONST_PERSONAL_REP = "PERSONAL_REP"
CONST_EXCEPTION_FILE = "EXCEPTION_FILE"
CONST_MARRIED_STATUS = "MARRIED_STATUS"
CONST_EDUCATION = "EDUCATION"
CONST_CIF_ID_TYPE = "CIF_ID_TYPE"
CONST_ADDRESS_TYPE = "ADDRESS_TYPE"
CONST_RELATIONSHIP = "RELATIONSHIP"
CONST_OWNER_PROPERTY = "OWNER_PROPERTY"
CONST_CUSTOMER_TYPE = "CUSTOMER_TYPE"
CONST_GENDER = "GENDER"
CONST_AVERAGE_INCOME = "AVERAGE_INCOME"
CONST_CUST_CLASSIFICATION = "CUST_CLASSIFICATION"
CONST_RESIDENT_STATUS = "RESIDENT_STATUS"
CONST_DEBT_CLASSIFICATION = "DEBT_CLASSIFICATION"
CONST_COLLATERAL_TYPE = "COLLATERAL_TYPE"
CONST_TYPE_TERM_LOAN = "TYPE_TERM_LOAN"
CONST_LOAN_PURPOSE = "LOAN_PURPOSE"
CONST_REMARK = "REMARK"
CONST_METHOD_RECEIVE_SALARY = "METHOD_RECEIVE_SALARY"
CONST_ABLE_PAY_LABEL = "ABLE_PAY_LABEL"
CONST_BUSINESS_TYPE_SH = "BUSINESS_TYPE_SH"
CONST_BUSINESS_TYPE = "BUSINESS_TYPE"
CONST_CONTRACT_TERM = "CONTRACT_TERM"
CONST_FREQUENCE = "FREQUENCE"
CONST_REPAY_PRINCIPAL_INTEREST = "REPAY_PRINCIPAL_INTEREST"
CONST_TYPE_REAL_ESTATE = "TYPE_REAL_ESTATE"
CONST_REAL_ESTATE_STATUS = "REAL_ESTATE_STATUS"
CONST_TYPE_EXCEPTION = "TYPE_EXCEPTION"
CONST_TYPE_RISK = "TYPE_RISK"
CONST_POLICY_DETAIL = "POLICY_DETAIL"
CONST_ACCEPT_CREDIT_LABEL = "ACCEPT_CREDIT_LABEL"
CONST_TYPE_TEMPLATE = "TYPE_TEMPLATE"
CONST_CUSTOMER_SEGMENT = "CUSTOMER_SEGMENT"
CONST_SCORE_RANK_DETAIL = "SCORE_RANK_DETAIL"
CONST_APPRAISAL_UNIT_TYPE_ID = "APPRAISAL_UNIT_TYPE_ID"
CONST_APPRAISAL_PURPOSE = "APPRAISAL_PURPOSE"
CONST_COLLATERAL_LOCATION_TYPE = "COLLATERAL_POSITION_TYPE"
CONST_ROAD_WIDTH = "ROAD_WIDTH"
CONST_COLLATERAl_CERTIFIED_TYPE = "COLLATERAL_CERTIFIED_TYPE"
CONST_COLLATERAL_OWNER_TYPE = "COLLATERAL_OWNER_TYPE"
CONST_PURPOSE_USING_LAND = "PURPOSE_USING_LAND"
CONST_ORIGIN_LAND_USE = "ORIGIN_LAND_USE"
CONST_LAND_USE_CERTIFIED = "LAND_USE_CERTIFIED"
CONST_CONSTRUCTION_PERMIT = "CONSTRUCTION_PERMIT"
CONST_CONSTRUCTION_TYPE = "CONSTRUCTION_TYPE"
CONST_COLLATERAL_CERTIFICATE_TYPE = "COLLATERAL_CERTIFICATE_TYPE"
CONST_LEGAL_STATUS = "LEGAL_STATUS"
CONST_PURPOSE_USE_LAND_VALUATION = "PURPOSE_USE_LAND_VALUATION"
CONST_TYPE_APARTMENT = "TYPE_APARTMENT"
CONST_VEHICLE_STATUS = "VEHICLE_STATUS"
CONST_DEVICES_PROPERTY_STATUS = "DEVICES_PROPERTY_STATUS"
CONST_GOODS_PROPERTY_STATUS = "GOODS_PROPERTY_STATUS"
CONST_RIGHT_PROPERTY_STATUS = "RIGHT_TO_PROPERTY_PROPERTY_STAT"
CONST_PAPER_TYPE = "PAPER_TYPE"
CONST_PROPERTY_TYPE = "PROPERTY_TYPE"
CONST_VEHICLE_TYPE = "VEHICLE_TYPE"
CONST_VEHICLE_DETAIL = "VEHICLE_DETAIL"
CONST_LIST_LEGAL_DOCUMENT = "LIST_LEGAL_DOCUMENT"
CONST_PRICE_APPRAISAL = "PRICE_APPRAISAL"
CONST_INDEPENDENT_VALUATION = "INDEPENDENT_VALUATION"
CONST_ISSUER = "ISSUER"
CONST_COUNTRY_MANUFACTURE = "COUNTRY_MANUFACTURE"
CONST_OTHER_COUNTRY_MANUFACTURE = "OTHER_COUNTRY_MANUFACT"


# NORMAL_LOAN
CONST_CAREERS = "CAREERS"
CONST_FATCA_INFO = "FATCA_INFO"
CONST_CREDIT_INSTITUTION = "CREDIT_INSTITUTION"
CONST_LOAN_PURPOSE_CORE = "LOAN_PURPOSE_CORE"
CONST_CURRENCY_TYPE = "CURRENCY_TYPE"
CONST_LENDING_METHOD = "LENDING_METHOD"
CONST_DISBURSEMENT = "DISBURSEMENT"
CONST_SCHEDULE = "SCHEDULE"
CONST_LOAN_INTEREST_RATE = "LOAN_INTEREST_RATE"
CONST_BUSINESS_LICENCE_TYPE = "BUSINESS_LICENCE_TYPE"
CONST_PAYMENT_METHOD = "PAYMENT_METHOD"
CONST_ASSET_TYPE = "ASSET_TYPE"
CONST_ACCEPT_STATUS = "ACCEPT_STATUS"
CONST_OTHER_CONTRACT_LABEL = "OTHER_CONTRACT_LABEL"
CONST_BUSINESS_REPRESENTATIVE = "BUSINESS_REPRESENTATIVE"
CONST_DOCUMENT_TYPE = "DOCUMENT_TYPE"


# LOAN_CREDIT
CONST_AUTHENTICATION_QUESTION = "AUTHENTICATION_QUESTION"
CONST_CUSTOMER_NEED = "CUSTOMER_NEED"
CONST_CARD_DELIVERY_METHOD = "CARD_DELIVERY_METHOD"
CONST_RELEASE_TYPE = "RELEASE_TYPE"
CONST_CARD_GUARANTEE_FORM = "CARD_GUARANTEE_FORM"
CONST_GIFT_CONDITION = "GIFT_CONDITION"
CONST_TYPE_CARD_USE = "TYPE_CARD_USE"
CONST_GIFT_SELECTION = "GIFT_SELECTION"
CONST_WORK_STATUS = "WORK_STATUS"


class Configs(str, Enum):
    countries = CONST_COUNTRIES
    provinces = CONST_PROVINCES
    districts = CONST_DISTRICTS
    wards = CONST_WARDS
    loan_product = CONST_LOAN_PRODUCT
    partner = CONST_PARTNER
    partner_product = CONST_PARTNER_PRODUCT
    personal_rep = CONST_PERSONAL_REP
    collateral_type = CONST_COLLATERAL_TYPE
    type_real_estate = CONST_TYPE_REAL_ESTATE
    type_exception = CONST_TYPE_EXCEPTION
    policy_detail = CONST_POLICY_DETAIL
    templates = CONST_TYPE_TEMPLATE
    credit_institution = CONST_CREDIT_INSTITUTION
    currency_type = CONST_CURRENCY_TYPE
    schedule = CONST_SCHEDULE
    issuer = CONST_ISSUER
    # collection_document = CONST_COLLECTION_DOCUMENT
    document_type = CONST_DOCUMENT_TYPE
    authen_question = CONST_AUTHENTICATION_QUESTION
    type_card_use = CONST_TYPE_CARD_USE
    gift_selection = CONST_GIFT_SELECTION
    score_rank_detail = CONST_SCORE_RANK_DETAIL
    property_type = CONST_PROPERTY_TYPE
    vehicle_type = CONST_VEHICLE_TYPE
    vehicle_detail = CONST_VEHICLE_DETAIL
    list_legal_document = CONST_LIST_LEGAL_DOCUMENT
    price_appraisal = CONST_PRICE_APPRAISAL
    independent_valuation = CONST_INDEPENDENT_VALUATION
    country_manufacture = CONST_COUNTRY_MANUFACTURE
    other_country_manufacture = CONST_OTHER_COUNTRY_MANUFACTURE


# List field in table udtm
FIELD_UDTM_LOV = {
    CONST_COLLATERAL: UDTM_QUESTION, CONST_EXCEPTION_FILE: UDTM_QUESTION, CONST_MARRIED_STATUS: UDTM_MARITAL_STATUS,
    CONST_EDUCATION: UDTM_EDUCATION, CONST_CIF_ID_TYPE: UDTM_CIF_ID_TYPE, CONST_ADDRESS_TYPE: UDTM_ADDRESS_TYPE,
    CONST_RELATIONSHIP: UDTM_RELATIONSHIP, CONST_OWNER_PROPERTY: UDTM_OWNER_PROPERTY, CONST_CUSTOMER_TYPE: UDTM_CUSTOMER_TYPE,
    CONST_GENDER: UDTM_SEX, CONST_AVERAGE_INCOME: UDTM_AVERAGE_INCOME, CONST_CUST_CLASSIFICATION: UDTM_CUST_CLASSIFICATION,
    CONST_RESIDENT_STATUS: UDTM_RESIDENT_STATUS, CONST_DEBT_CLASSIFICATION: UDTM_DEBT_CLASSIFICATION, CONST_TYPE_TERM_LOAN: UDTM_PRODUCT_CATEGORY,
    CONST_LOAN_PURPOSE: UDTM_PRODUCT_LOAN_PURPOSE, CONST_REMARK: UDTM_REMARK, CONST_METHOD_RECEIVE_SALARY: UDTM_DISBURSEMENT,
    CONST_ABLE_PAY_LABEL: UDTM_ABLE_PAY_LABEL, CONST_BUSINESS_TYPE_SH: UDTM_BUSINESS_TYPE_SH, CONST_BUSINESS_TYPE: UDTM_BUSINESS_TYPE,
    CONST_CONTRACT_TERM: UDTM_CONTRACT_TERM, CONST_FREQUENCE: UDTM_FREQUENCE, CONST_REPAY_PRINCIPAL_INTEREST: UDTM_ACCEPT_FLAG,
    CONST_REAL_ESTATE_STATUS: UDTM_REAL_ESTATE_STATUS, CONST_TYPE_RISK: UDTM_RISK_TYPE, CONST_ACCEPT_CREDIT_LABEL: UDTM_ACCEPT_CREDIT_LABEL,
    CONST_CAREERS: UDTM_CAREER, CONST_FATCA_INFO: UDTM_FATCA_INFO, CONST_LOAN_PURPOSE_CORE: UDTM_LOAN_PURPOSE_CORE, CONST_LENDING_METHOD: UDTM_LENDING_METHOD,
    CONST_DISBURSEMENT: UDTM_DISBURSEMENT, CONST_LOAN_INTEREST_RATE: UDTM_SCHEDULE_UNIT, CONST_BUSINESS_LICENCE_TYPE: UDTM_BUSINESS_LICENCE_TYPE,
    CONST_PAYMENT_METHOD: UDTM_PAYMENT, CONST_ASSET_TYPE: UDTM_ASSET_RENT_TYPE, CONST_ACCEPT_STATUS: UDTM_ACCEPT_STATUS,
    CONST_OTHER_CONTRACT_LABEL: UDTM_USED_OTHER_CONTRACT_LABEL, CONST_BUSINESS_REPRESENTATIVE: UDTM_BUSINESS_REPRESENTATIVE,
    CONST_CUSTOMER_SEGMENT: CIC_CUS_SEGMENT, CONST_CUSTOMER_NEED: UDTM_CUSTOMER_NEED, CONST_CARD_DELIVERY_METHOD: UDTM_CARD_DELIVERY_METHOD,
    CONST_RELEASE_TYPE: UDTM_PUBLICATION_SPEED_TYPE, CONST_CARD_GUARANTEE_FORM: UDTM_CURRENT_CARD_GUARANTEE_FORM,
    CONST_GIFT_CONDITION: UDTM_QUESTION, CONST_APPRAISAL_UNIT_TYPE_ID: VALUATION_UNIT_TYPE, CONST_APPRAISAL_PURPOSE: COLLATERAL_VALUATION_PURPOSE,
    CONST_COLLATERAL_LOCATION_TYPE: COLLATERAL_LOCATION_TYPE, CONST_ROAD_WIDTH: COLLATERAL_LANE_WIDTH, CONST_COLLATERAl_CERTIFIED_TYPE: COLLATERAL_LAND_CERT_TYPE,
    CONST_COLLATERAL_OWNER_TYPE: UDTM_COLLATERAL_OWNER_TYPE, CONST_PURPOSE_USING_LAND: COLLATERAL_LAND_ASSET_VALUATION_LAND_USE_PURPOSE,
    CONST_ORIGIN_LAND_USE: COLLATERAL_CERT_LAND_USE_SOURCE, CONST_LAND_USE_CERTIFIED: COLLATERAL_CERT_LAND_USE_FORM,
    CONST_CONSTRUCTION_PERMIT: COLLATERAL_LAND_ASSET_LEGAL, CONST_CONSTRUCTION_TYPE: COLLATERAL_LAND_ASSET_TYPE,
    CONST_COLLATERAL_CERTIFICATE_TYPE: COLLATERAL_CONST_CERT_TYPE, CONST_LEGAL_STATUS: COLLATERAL_APARTMENT_LEGAL_STATUS,
    CONST_PURPOSE_USE_LAND_VALUATION: COLLATERAL_APARTMENT_VALUATION_LAND_USE_PURPOSE, CONST_TYPE_APARTMENT: COLLATERAL_APARTMENT_TYPE,
    CONST_VEHICLE_STATUS: COLLATERAL_TRANS_STATUS, CONST_DEVICES_PROPERTY_STATUS: COLLATERAL_MACHINE_STATUS, CONST_GOODS_PROPERTY_STATUS: COLLATERAL_CARGO_STATUS,
    CONST_RIGHT_PROPERTY_STATUS: COLLATERAL_RIGHT_PROPERTY_STATUS, CONST_PAPER_TYPE: COLLATERAL_BALANCE_TYPE, CONST_WORK_STATUS: UDTM_WORK_STATUS
}


# Handle response for configs
FUNC_RESPONSE = [
    CONST_DISTRICTS, CONST_WARDS, CONST_LOAN_PRODUCT, CONST_PARTNER_PRODUCT, CONST_PERSONAL_REP, CONST_BUSINESS_TYPE, CONST_TYPE_EXCEPTION,
    CONST_POLICY_DETAIL, CONST_CAREERS, CONST_PARTNER, CONST_DOCUMENT_TYPE, CONST_AUTHENTICATION_QUESTION, CONST_TYPE_CARD_USE, CONST_GIFT_SELECTION,
    CONST_VEHICLE_DETAIL
]
