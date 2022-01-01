from fastapi import FastAPI, status
from . import models
from .database import engine
from .routers import post, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost/*",
    "http://localhost:8080/*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "API Root"}
