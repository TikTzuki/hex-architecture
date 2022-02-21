from enum import Enum

from app.utils.constant.utils import LOAN_TYPE_CARD, LOAN_TYPE_NORMAL


class ETemplateType(str, Enum):
    OLD_NORMAL_LOAN_TEMPLATE = f"OLD_{LOAN_TYPE_NORMAL}"
    NORMAL_LOAN = LOAN_TYPE_NORMAL
    CARD_LOAN = LOAN_TYPE_CARD
