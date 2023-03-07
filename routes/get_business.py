from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/v1/business")
async def get_business_controller():
    return JSONResponse(content=dict(message="Retrieved business detail successfully"), status_code=status.HTTP_200_OK)
