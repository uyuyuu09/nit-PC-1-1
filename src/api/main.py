import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.api.v1 import questions_api


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions_api.router)


@app.get(
    "/",
    tags=["root"],
    responses={
        200: {
            "description": "Root path",
            "content": {"application/json": {"example": {"status": "ok"}}},
        },
    },
)
async def root():
    """
    This is the root path of the backend server.
    """
    return JSONResponse(content={"status": "ok", "hello": "world"})


@app.get(
    "/health",
    tags=["health"],
    responses={
        200: {
            "description": "Health check",
            "content": {"application/json": {"example": {"status": "ok"}}},
        },
    },
)
async def health_check():
    """
    This is a health check endpoint.
    """
    try:
        return JSONResponse(content={"status": "pass"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})


if __name__ == "__main__":
    uvicorn.run(app=app)
