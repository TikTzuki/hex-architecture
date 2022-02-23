from database.models.asset.real_estate.model import AssetRealEstate
from database.models.asset.real_transportation.model import AssetTransportation
from database.models.business_finance_cashflow.model import BusinessFinanceCashflow
from database.models.business_finance_cashflow.value.model import BusinessFinanceCashflowValue
from database.models.business_finance_cashflow.vendor.model import BusinessFinanceCashflowVendor
from database.models.asset.other.model import AssetOther
from database.models.collateral.model import Collateral
from database.models.credit.card.model import CreditCard
from database.models.credit.collateral.model import CreditCollateral
from database.models.credit.institution.model import CreditInstitution, CreditInstitutionLoan
from database.models.cytm_ccy_defn_master.model import CytmCcyDefnMaster
from database.models.finance.matadata.model import FinanceMetadata, FinanceMetadataGroup, FinanceMetadataItem
from database.models.finance.timeline.model import FinanceTimeline, FinanceTimelineAssign
from database.models.income_squence.model import IncomeSequence
from database.models.ma.cic_score.model import MaCicScoreDetail, MaCicScore

from database.models.ma.group_cust.model import MaCreditGroupCustomerItem, MaCreditGroupCustomer

from database.models.ma.card_promotion.model import MaCardPromotion

from database.models.ma.question.model import MaQuestion

from database.models.ma.document_type.model import MaDocumentType

from database.models.ma.customer_type.model import MaCustomerType
from database.models.partner.model import PartnerLoanProduct, Partner, PartnerProduct
from database.models.person.credit_score.model import PersonCreditScore, PersonCreditScoreSegment
from database.models.product.document_rule.model import ProductDocumentRule
from database.models.product.promotion.model import ProductPromotion
from database.models.product.question.model import ProductQuestion
from database.models.profile.answer_cust.model import ProfileAnswerCus
from database.models.profile.credit.card_delivery.model import ProfileCreditCardDelivery
from database.models.profile.credit.modified.model import ProfileCreditModified
from database.models.profile.credit.promotion.model import ProfileCreditPromotion
from database.models.profile.credit.published.model import ProfileCreditPublished
from database.models.profile.credit.squence_item.model import ProfileCreditSequenceItem
from database.models.profile.credit.statement_method.model import ProfileCreditStatementMethod
from database.models.profile.credit.supp_card.model import ProfileCreditSuppCard
from database.models.profile.document.model import ProfileDocument
from database.models.profile.model import Profile
from database.models.profile.score.model import ProfileScore
from database.models.profile.squence_item.model import ProfileSequenceItem
from database.models.source_income.business_household.model import SourceIncomeBusinessHousehold
from database.models.source_income.company.model import SourceIncomeCompany
from database.models.source_income.deposit.model import SourceIncomeDeposit
from database.models.source_income.group_asset.model import SourceIncomeGroupAsset
from database.models.source_income.other.model import SourceIncomeOther
from database.models.source_income.pension.model import SourceIncomePension
from database.models.source_income.salary.model import SourceIncomeSalary
from database.models.source_income.stock.model import SourceIncomeStock
from database.models.sttm.regional_office.model import RegionalOffice
from database.models.udtm_lov.model import UdtmLov

__all__ = [
    AssetOther,
    AssetRealEstate,
    AssetTransportation,
    BusinessFinanceCashflow,
    BusinessFinanceCashflowVendor,
    BusinessFinanceCashflowValue,
    CollateralCargo,
    CollateralMachine,
    CollateralOther,
    CollateralOwner,
    CollateralPaper,
    CollateralApartment,
    CollateralLandAsset,
    CollateralMarket,
    CollateralLand,
    CollateralRealEstate,
    CollateralRightProperty,
    CollateralStock,
    CollateralTransportation,
    Collateral,
    CreditCard,
    CreditCollateral,
    CreditInstitution,
    CreditInstitutionLoan,
    CytmCcyDefnMaster,
    FinanceMetadata,
    FinanceMetadataGroup,
    FinanceMetadataItem,
    FinanceTimeline,
    FinanceTimelineAssign,
    IncomeSequence,
    UdtmLov,
    # District,
    # Country,
    # Branch,
    # Province,
    # Ward,
    SourceIncomePension,
    SourceIncomeStock,
    SourceIncomeSalary,
    SourceIncomeOther,
    SourceIncomeGroupAsset,
    SourceIncomeDeposit,
    SourceIncomeCompany,
    SourceIncomeBusinessHousehold,
    Profile,
    ProfileRiskItem,
    ProfileIncome,
    ProfileExceptionItem,
    ProfileCost,
    Policy,
    PolicyRule,
    PolicyGroup,
    PolicyDetail,
    Person,
    PersonalRelationship,
    PersonMarried,
    PersonIdentity,
    PersonGroupIncome,
    PersonFccCore,
    PersonEducation,
    PersonCreditInstitutionRelationship,
    PersonBusiness,
    PersonBusinessFinanceReport,
    PersonBusinessAddress,
    PersonAddress,
    MaBusinessLine,
    MaFrequence,
    LoanProduct,
    LoanProductPolicy,
    DetmClgBrnCode,
    MaBankCode,
    GetmCollCategory,
    MaPersonalRep,
    MaCollType,
    MaBusinessType,
    MaCustomerType,
    Partner,
    PartnerProduct,
    PartnerLoanProduct,
    ProfileSequenceItem,
    ProfileScore,
    MaDocumentType,
    MaQuestion,
    ProductDocumentRule,
    ProductQuestion,
    ProfileAnswerCus,
    ProfileDocument,
    MaCreditGroupCustomer,
    ProfileCreditModified,
    ProfileCreditPublished,
    ProfileCreditSequenceItem,
    ProfileCreditSuppCard,
    MaCardPromotion,
    ProductPromotion,
    ProfileCreditCardDelivery,
    ProfileCreditPromotion,
    MaCreditGroupCustomerItem,
    PersonCreditScoreSegment,
    PersonCreditScore,
    MaCicScore,
    MaCicScoreDetail,
    RegionalOffice,
    ProfileCreditStatementMethod
]
