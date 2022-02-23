from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import VARCHAR2

from database import Base


class GetmCollCategory(Base):
    __tablename__ = 'ud_los_getm_coll_category'

    id = Column("ID", Integer, primary_key=True)

    category_name = Column("CATEGORY_NAME", VARCHAR2(50))

    description = Column("DESCRIPTION", VARCHAR2(105))

    coll_type_id = Column("COLL_TYPE_ID", Integer)

    category_type = Column("CATEGORY_TYPE", VARCHAR2(1))

    secured = Column("SECURED", VARCHAR2(1))

    review_date = Column("REVIEW_DATE", DateTime)

    tangible = Column("TANGIBLE", VARCHAR2(1))

    reval_frequency = Column("REVAL_FREQUENCY", VARCHAR2(50))

    reval_due_date = Column("REVAL_DUE_DATE", Integer)

    reval_start_month = Column("REVAL_START_MONTH", VARCHAR2(3))

    remarks = Column("REMARKS", VARCHAR2(255))

    record_stat = Column("RECORD_STAT", VARCHAR2(1))

    auth_stat = Column("AUTH_STAT", VARCHAR2(1))

    mob_no = Column("MOD_NO", Integer)

    maker_id = Column("MAKER_ID", VARCHAR2(50))

    maker_dt_stamp = Column("MAKER_DT_STAMP", DateTime)

    checker_id = Column("CHECKER_ID", VARCHAR2(50))

    checker_dt_stamp = Column("CHECKER_DT_STAMP", DateTime)

    once_auth = Column("ONCE_AUTH", VARCHAR2(1))

    source = Column("SOURCE", VARCHAR2(35))

    user_refno = Column("USER_REFNO", VARCHAR2(50))

    udf_value_1 = Column("UDF_VALUE_1", VARCHAR2(4000))

    udf_value_2 = Column("UDF_VALUE_2", VARCHAR2(4000))

    udf_value_3 = Column("UDF_VALUE_3", VARCHAR2(4000))

    udf_value_4 = Column("UDF_VALUE_4", VARCHAR2(4000))

    udf_value_5 = Column("UDF_VALUE_5", VARCHAR2(4000))

    udf_value_6 = Column("UDF_VALUE_6", VARCHAR2(4000))

    udf_value_7 = Column("UDF_VALUE_7", VARCHAR2(4000))

    udf_value_8 = Column("UDF_VALUE_8", VARCHAR2(4000))

    udf_value_9 = Column("UDF_VALUE_9", VARCHAR2(4000))

    udf_value_10 = Column("UDF_VALUE_10", VARCHAR2(4000))

    udf_value_11 = Column("UDF_VALUE_11", VARCHAR2(4000))

    udf_value_12 = Column("UDF_VALUE_12", VARCHAR2(4000))

    udf_value_13 = Column("UDF_VALUE_13", VARCHAR2(4000))

    udf_value_14 = Column("UDF_VALUE_14", VARCHAR2(4000))

    udf_value_15 = Column("UDF_VALUE_15", VARCHAR2(4000))

    udf_value_16 = Column("UDF_VALUE_16", VARCHAR2(4000))

    udf_value_17 = Column("UDF_VALUE_17", VARCHAR2(4000))

    udf_value_18 = Column("UDF_VALUE_18", VARCHAR2(4000))

    udf_value_19 = Column("UDF_VALUE_19", VARCHAR2(4000))

    udf_value_20 = Column("UDF_VALUE_20", VARCHAR2(4000))

    udf_value_21 = Column("UDF_VALUE_21", VARCHAR2(4000))

    udf_value_22 = Column("UDF_VALUE_22", VARCHAR2(4000))

    udf_value_23 = Column("UDF_VALUE_23", VARCHAR2(4000))

    udf_value_24 = Column("UDF_VALUE_24", VARCHAR2(4000))

    udf_value_25 = Column("UDF_VALUE_25", VARCHAR2(4000))

    udf_value_26 = Column("UDF_VALUE_26", VARCHAR2(4000))

    udf_value_27 = Column("UDF_VALUE_27", VARCHAR2(4000))

    udf_value_28 = Column("UDF_VALUE_28", VARCHAR2(4000))

    udf_value_29 = Column("UDF_VALUE_29", VARCHAR2(4000))

    udf_value_30 = Column("UDF_VALUE_30", VARCHAR2(4000))

    udf_value_31 = Column("UDF_VALUE_31", VARCHAR2(4000))

    udf_value_32 = Column("UDF_VALUE_32", VARCHAR2(4000))

    udf_value_33 = Column("UDF_VALUE_33", VARCHAR2(4000))

    udf_value_34 = Column("UDF_VALUE_34", VARCHAR2(4000))

    udf_value_35 = Column("UDF_VALUE_35", VARCHAR2(4000))

    udf_value_36 = Column("UDF_VALUE_36", VARCHAR2(4000))

    udf_value_37 = Column("UDF_VALUE_37", VARCHAR2(4000))

    udf_value_38 = Column("UDF_VALUE_38", VARCHAR2(4000))

    udf_value_39 = Column("UDF_VALUE_39", VARCHAR2(4000))

    udf_value_40 = Column("UDF_VALUE_40", VARCHAR2(4000))

    udf_value_41 = Column("UDF_VALUE_41", VARCHAR2(4000))

    udf_value_42 = Column("UDF_VALUE_42", VARCHAR2(4000))

    udf_value_43 = Column("UDF_VALUE_43", VARCHAR2(4000))

    udf_value_44 = Column("UDF_VALUE_44", VARCHAR2(4000))

    udf_value_45 = Column("UDF_VALUE_45", VARCHAR2(4000))

    udf_value_46 = Column("UDF_VALUE_46", VARCHAR2(4000))

    udf_value_47 = Column("UDF_VALUE_47", VARCHAR2(4000))

    udf_value_48 = Column("UDF_VALUE_48", VARCHAR2(4000))

    udf_value_49 = Column("UDF_VALUE_49", VARCHAR2(4000))

    udf_value_50 = Column("UDF_VALUE_50", VARCHAR2(4000))
