from fastapi import APIRouter

router = APIRouter()


@router.get("/{user_id}/")
def get_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}
