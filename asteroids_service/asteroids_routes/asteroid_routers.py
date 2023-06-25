from fastapi import APIRouter, Depends

from asteroids_service.integration.asteroid import AsteroidService
from asteroids_service.service.dependencies import asteroid_feed_dependency

router = APIRouter(
    prefix="/api",
    tags=["nasa"],
    responses={404: {"description": "Not found"}},
)


@router.get("/asteroids/{start_date}/{end_date}", response_model=None)
async def get_feed(
        start_date: str, end_date: str, asteroid_service: AsteroidService = Depends(asteroid_feed_dependency)
):
    return await asteroid_service(start_date, end_date)
