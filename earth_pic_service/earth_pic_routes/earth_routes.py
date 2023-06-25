from fastapi import APIRouter, Depends

from earth_pic_service.integration.earth import EarthService
from earth_pic_service.service.dependencies import earth_pic_dependency

router = APIRouter(
    prefix="/api",
    tags=["nasa"],
    responses={404: {"description": "Not found"}},
)


@router.get('/earth/city', response_model=None)
async def show_earth(
        date: str, city: str, earth_service: EarthService = Depends(earth_pic_dependency)
):
    return await earth_service(date, city)
