from fastapi import APIRouter
from helloworldapp.api.v1.endpoints import story, user

router = APIRouter()

router.include_router(story.router, prefix="/story", tags=["story"])
router.include_router(user.router, prefix="/user", tags=["user"])
