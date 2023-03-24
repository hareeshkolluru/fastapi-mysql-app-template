import uvicorn
from fastapi import FastAPI
from loguru import logger

from helloworldapp import settings
from helloworldapp.api.v1.api import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"/{settings.API_V1_STR}/openapi.json",
)

app.include_router(router, prefix=f"/{settings.API_V1_STR}")


def start():
    """Launch API server."""
    logger.info("Starting API server.")
    uvicorn.run(
        "helloworldapp.main:app",
        host=settings.URL,
        port=settings.PORT,
        reload=True,
    )


if __name__ == "__main__":
    start()
