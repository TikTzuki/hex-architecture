from enum import Enum

# Loại quan hệ
LEGAL_TYPE_BORROWER = "BORROWER"  # "NGUOI_VAY_CHINH"
LEGAL_TYPE_MARRIAGE = "MARRIAGE"  # "NGUOI_HON_PHOI"
LEGAL_TYPE_CO_BORROWER = "CO_BRW"  # "NGUOI_DONG_VAY"
LEGAL_TYPE_CO_PAYER = "CO_PAYER"  # "NGUOI_DONG_TRA_NO"
LEGAL_TYPE_LAW_RELATED = "LAW_RLT"  # "NGUOI_LIEN_QUAN_THEO_QDPL"
LEGAL_TYPE_RELATED = "RELATED"  # "NGUOI_LIEN_HE"
LEGAL_TYPE_OTHER = "OTHER"  # "DOI_TUONG_KHAC"

# quốc tịch
COUNTRY = 'COUNTRY'
# loại giấy tờ
CIF_ID_TYPE = "CIF_ID_TYPE"


class ERelationshipType(str, Enum):
    """
        Loại quan hệ trong hồ sơ
        Table: LOS_MA_PERSONAL_REP
    """
    BORROWER = LEGAL_TYPE_BORROWER
    MARRIAGE = LEGAL_TYPE_MARRIAGE
    CO_BORROWER = LEGAL_TYPE_CO_BORROWER
    CO_PAYER = LEGAL_TYPE_CO_PAYER
    LAW_RELATED = LEGAL_TYPE_LAW_RELATED
    RELATED = LEGAL_TYPE_RELATED


class EPersonType(str, Enum):
    """
        Loại quan hệ trong hồ sơ
        Table: LOS_MA_PERSONAL_REP
    """
    BORROWER = LEGAL_TYPE_BORROWER
    MARRIAGE = LEGAL_TYPE_MARRIAGE
    CO_BORROWER = LEGAL_TYPE_CO_BORROWER
    CO_PAYER = LEGAL_TYPE_CO_PAYER
    LAW_RELATED = LEGAL_TYPE_LAW_RELATED
    RELATED = LEGAL_TYPE_RELATED
    OTHERS = LEGAL_TYPE_OTHER