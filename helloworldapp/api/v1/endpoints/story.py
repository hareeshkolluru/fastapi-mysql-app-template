from fastapi import APIRouter

router = APIRouter()


@router.get("/{story_id}/")
def get_story(story_id: int) -> dict[str, int]:
    return {"story_id": story_id}
