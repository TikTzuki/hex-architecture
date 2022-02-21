import logging
import os
import sys
from typing import List, Dict

from loguru import logger
from pydantic import Field, BaseSettings, BaseModel
from pydantic.main import object_setattr

from project.settings.logging_config import InterceptHandler


class ApplicationSettings(BaseSettings):
    version: str = Field("1.0.0")
    project_name: str = Field("Los", env="PROJECT_NAME")
    description: str = Field("LOS description")
    secret_key: str = Field("", env="SECRET_KEY")
    debug: bool = Field(True, env="DEBUG")
    allowed_hosts: List = Field(["*"], env="ALLOWED_HOSTS")
    LANGUAGE_CODE: str = Field('en-us')
    TIME_ZONE: str = Field('UTC')
    USE_I18N: bool = Field(True)
    USE_TZ: bool = Field(True)


class DatabaseSettings(BaseSettings):
    class Oracle(BaseModel):
        host: str = Field("192.168.74.66", env="ORACLE_HOST")
        port: str = Field("1521", env="ORACLE_PORT")
        username: str = Field("los", env="ORACLE_USERNAME")
        password: str = Field("123456", env="ORACLE_PASSWORD")
        service_name: str = Field("los", env="ORACLE_DATABASE")

    class Mongo(BaseModel):
        host: str = Field("localhost", env="MONGO_HOST")
        port: str = Field("27017", env="MONGO_PORT")
        username: str = Field("root", env="MONGO_USERNAME")
        password: str = Field("root", env="MONGO_PASSWORD")
        database: str = Field("admin", env="MONGO_DATABASE")

    oracle: Oracle = Oracle()
    mongo: Mongo = Mongo()


class RedisSettings(BaseSettings):
    host: str = Field('192.168.73.149', env="REDIS_HOST")
    port: int = Field(6379, env="REDIS_PORT")
    password: str = Field("dbsystem535", env="REDIS_PASSWORD")
    ttl: int = Field(30, env="REDIS_TTL")
    db_configs: int = Field(1, env="REDIS_DATABASE")


class ServiceSettings(BaseSettings):
    class Location(BaseModel):
        url: str = Field(f"http://superapp.minerva.vn:9213/")
        header: Dict = Field({
            "Connection": "keep-alive",
            "MNV-encode": "0",
            "DNT": "1",
            "MNV-LANGUAGE": "en",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
            "content_type": "application/json; charset=utf-8",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7",
        })

    class LDAP(BaseModel):
        host: str = Field("192.168.73.57", env="LDAP_HOST")
        port: int = Field(636, env="LDAP_PORT")

    class DBS(BaseModel):
        host: str = Field(f"http://192.168.73.135:9004", env="DBS_SERVICE_HOST")
        datetime_format: str = Field("%d/%m/%Y %H:%M:%S")
        server_auth: str = Field(f"2L0YHOzA4NqqavbYyAwQ7k0cz0X1BbPF", env="DBS_SERVICE_AUTH")
        authorization: str = Field("bearer 1")

    class File(BaseModel):
        file_limit: int = Field(10, env="FILE_LIMIT")
        file_size_min: int = Field(1, env="FILE_SIZE_MIN")
        file_size_max: int = Field(2_000_000, env="FILE_SIZE_MAX")
        file_size_measure: str = Field("bytes")
        extensions: List[str] = Field([".csv", ".doc", ".docx", ".jpeg", ".jpg", ".png", ".pdf", ".ppt", ".pptx", ".rtf", ".svg", ".txt", ".xls", ".xlsx"])
        mimetypes: List[str] = Field([
            "text/csv",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "image/jpeg",
            "image/png",
            "application/pdf",
            "application/vnd.ms-powerpoint",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "image/svg+xml",
            "text/plain",
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ])

    class Template(BaseModel):
        host: str = Field(f"http://192.168.73.135:9002", env="TEMPLATE_SERVICE_HOST")
        server_auth = Field(f"Zji3TMBsgtDKNzuFefi1So6Xr1YPzgXp", env="TEMPLATE_SERVICE_AUTH")

    location = Location()
    ldap = LDAP()
    dbs = DBS()
    file = File()
    template = Template()


APPLICATION = ApplicationSettings()

DATABASES = DatabaseSettings()

REDIS = RedisSettings()

SERVICE = ServiceSettings()

print(sys.getsizeof(SERVICE))

print(sys.getsizeof({
    "location": {
        "url": f"http://superapp.minerva.vn:9213/",  # noqa
        "headers": {
            "Connection": "keep-alive",
            "MNV-encode": "0",
            "DNT": "1",
            "MNV-LANGUAGE": "en",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
            "content_type": "application/json; charset=utf-8",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7",
        }
    },
    'ldap': {
        "host": os.getenv("LDAP_HOST", "192.168.73.57"),
        "port": os.getenv("LDAP_PORT", 636),
    },
    "dbs-service": {
        "host": os.getenv("DBS_SERVICE_HOST", f"http://192.168.73.135:9004"),  # noqa
        "datetime-format": "%d/%m/%Y %H:%M:%S",
        "server-auth": os.getenv("DBS_SERVICE_AUTH", f"2L0YHOzA4NqqavbYyAwQ7k0cz0X1BbPF"),  # noqa
        "authorization": "bearer 1"
    },
    "file-upload": {
        "file_limit": int(os.getenv("FILE_LIMIT", 10)),
        "file_size_min": int(os.getenv("FILE_SIZE_MIN", 1)),
        "file_size_max": int(os.getenv("FILE_SIZE_MAX", 2000_000)),
        "file_size_measure": "bytes",
        "extensions": [".csv", ".doc", ".docx", ".jpeg", ".jpg", ".png", ".pdf", ".ppt", ".pptx", ".rtf", ".svg",
                       ".txt", ".xls", ".xlsx"],
        "mime": [
            "text/csv",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "image/jpeg",
            "image/png",
            "application/pdf",
            "application/vnd.ms-powerpoint",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "image/svg+xml",
            "text/plain",
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ]
    },
    "template-service": {
        "host": os.getenv("TEMPLATE_SERVICE_HOST", f"http://192.168.73.135:9002"),  # noqa
        "server-auth": os.getenv("TEMPLATE_SERVICE_AUTH", f"Zji3TMBsgtDKNzuFefi1So6Xr1YPzgXp"),  # noqa
    },
}))

# logging configuration
LOGGING_LEVEL = logging.DEBUG if APPLICATION.debug else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access", "sqlalchemy.engine")
logger.level("CUSTOM", no=15, color="<blue>", icon="@")
logger.level("SERVICE", no=200)

logging.getLogger().handlers = [InterceptHandler()]
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": LOGGING_LEVEL},
        {
            "sink": sys.stderr,
            "level": 200,
            "format": "<blue>{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}</blue>",
        },
    ]
)
