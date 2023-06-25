import uvicorn
from fastapi import FastAPI

from apod_service.routes import apod_routes
from asteroids_service.asteroids_routes import asteroid_routers

app = FastAPI()
app.include_router(apod_routes.router)
app.include_router(asteroid_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
