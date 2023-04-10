from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.routing import APIRouter

from maxpath import MaxPathService
from models import TreeData

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.post("/max-path-sum")
def max_path_sum(
    data: TreeData, service: Annotated[MaxPathService, Depends(MaxPathService)]
) -> dict[str, int]:
    result = service.find_max_path_sum(data)
    return {"result": result}


app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
