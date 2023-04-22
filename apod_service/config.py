from pydantic import BaseSettings


class ApodConfig(BaseSettings):
    apod_pic_service: str = "FW6HkzJlBHzEZZnqsBuLu5K8TpGWvRpmM0Vwflx1"
