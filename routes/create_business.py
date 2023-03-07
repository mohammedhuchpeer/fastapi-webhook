from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/v1/business")
async def create_business_controller():
    return JSONResponse(content={"details": "request_id"}, status_code=status.HTTP_200_OK)
