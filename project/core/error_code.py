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
ID_NOT_FOUND = "ID_NOT_FOUND "

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
    DATABASE_INSERT_FAILED: "database insert failed",
    QUERY_DATA_ERROR: "query data error",
    CREATE_ERROR: "create error",
    UPDATE_ERROR: "update error",
    NOT_FOUND: "not found",
    ID_NOT_FOUND: "id {id} not found",

    DOCUMENT_NOT_EXISTS: "document not exists!",
    SERVICE_ERROR: "service error",
    KEY_ERROR: "key error",
    BAD_REQUEST: "bad request",
    ID_ALREADY_EXIST_ERROR: "id already exist"
}
