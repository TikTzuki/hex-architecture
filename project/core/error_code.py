# datetime error
DATE_NOT_GT = "DATE_NOT_GT"
DATE_NOT_GE = "DATE_NOT_GE"
DATE_NOT_LT = "DATE_NOT_LT"
DATE_NOT_LE = "DATE_NOT_LE"
# database
DATABASE_INSERT_FAILED = "DATABASE_INSERT_FAILED"
QUERY_DATA_ERROR = "QUERY_DATA_ERROR"
CREATE_ERROR = "CREATE_ERROR"
UPDATE_ERROR = "UPDATE_ERROR"
NOT_FOUND = "NOT_FOUND"

DOCUMENT_NOT_EXISTS = "DOCUMENT_NOT_EXISTS"
SERVICE_ERROR = "SERVICE_ERROR"
KEY_ERROR = "KEY_ERROR"
BAD_REQUEST = "BAD_REQUEST"
ID_ALREADY_EXIST_ERROR = "ID_ALREADY_EXIST_ERROR"

msg_templates = {
    # datetime error
    DATE_NOT_GT: "ensure this value is greater then {limit_value}",
    DATE_NOT_GE: "ensure this value is greater or equal to {limit_value}",
    DATE_NOT_LT: "ensure this value is less than {limit_value}",
    DATE_NOT_LE: "ensure this value is less than or equal to {limit_value}",
    # database
    DATABASE_INSERT_FAILED: "Database insert failed",
    QUERY_DATA_ERROR: "Query data error",
    CREATE_ERROR: "Create error",
    UPDATE_ERROR: "Update error",
    NOT_FOUND: "Not found",

    DOCUMENT_NOT_EXISTS: "Document not exists!",
    SERVICE_ERROR: "Service error",
    KEY_ERROR: "Key error",
    BAD_REQUEST: "Bad request",
    ID_ALREADY_EXIST_ERROR: "ID already exist"
}
