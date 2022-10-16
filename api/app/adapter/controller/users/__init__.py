from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from ...middleware import token

router = APIRouter()


@router.get(
    "/",
    dependencies=[Depends(token.get_token_header)],
)
async def read_users():
    # return JSONResponse(status_code=404)
    # return JSONResponse(status_code=404, content={"message": "Item not found"})
    return [{"username": "Tom"}, {"username": "Black"}]
