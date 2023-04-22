from typing import Any, List, Coroutine

from fastapi import APIRouter, Depends
from apod_service.dependencies import apod_pic_dependency
from apod_service.inegration.apod_service import ApodResponse
from apod_service.services.apod import ApodService

router = APIRouter(
    prefix="/api",
    tags=["nasa"],
    responses={404: {"description": "Not found"}},
)


@router.get("/apod/{date}", response_model=ApodResponse)
async def get_pic(
        date: str, hd: bool, apod_service: ApodService = Depends(apod_pic_dependency)
) -> ApodResponse:
    return await apod_service(date, hd)

