from fastapi import APIRouter
from loguru import logger

from utils.context import get_request_id

router = APIRouter()


@router.get('/v1/healthcheck')
async def healthcheck_controller():
    request_id = get_request_id()
    logger.info(f"Request reached the healthcheck route for rid: {request_id}")
    return dict(message="server running successfully")
