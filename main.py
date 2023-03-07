import uuid

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from loguru import logger

from routes import healthcheck, create_business
from utils.context import request_id_ctx_var

MESSAGE_STREAM_DELAY = 1  # second
MESSAGE_STREAM_RETRY_TIMEOUT = 15000
app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request_id_ctx_var.set(request_id)
    logger.info(f"Raised the request with rid: {request_id}")
    try:
        response = await call_next(request)
    except Exception as error:
        response = JSONResponse(content={"details": "something went wrong", "error": error},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        response.headers['X-Request-ID'] = request_id
        logger.info(f"Request completed for rid: {request_id}")
        return response


@app.get('/')
async def root_get(request: Request):
    print(request)
    return JSONResponse(content={"message": "Hello World"}, status_code=200)


COUNTER = 0


def get_message():
    global COUNTER
    COUNTER += 1
    return COUNTER, COUNTER < 21


app.include_router(create_business.router)
app.include_router(healthcheck.router)
