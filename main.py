import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from project import router
from project.core.exception import LOSException
from project.settings.configs import APPLICATION
from project.settings.middleware import middleware_setting

app = FastAPI(
    title=APPLICATION.project_name,
    description=APPLICATION.description,
    debug=APPLICATION.debug,
    version=APPLICATION.version,
    docs_url="/",
    default_response_class=ORJSONResponse
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=APPLICATION.allowed_hosts or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["POST", "GET"],
)

app.include_router(router=router.router, prefix="/api/v1")


@app.middleware("http")
async def time_header(request: Request, call_next):
    return await middleware_setting(request=request, call_next=call_next)


@app.exception_handler(LOSException)
async def los_http_exception_handler(request: Request, exc: LOSException):
    return ORJSONResponse(
        content={
            "errors": exc.get_detail(),
        },
        status_code=exc.status_code,
        headers=exc.headers
    )


@app.exception_handler(RequestValidationError)
async def except_custom(request: Request, exc: RequestValidationError):  # noqa
    return ORJSONResponse(
        content={
            "errors": LOSException.errors_pipeline(exc.errors())
        },
        status_code=status.HTTP_400_BAD_REQUEST,
    )


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True, env_file=".env")
