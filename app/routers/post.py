from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/posts", status_code=status.HTTP_200_OK, response_model=list[schemas.PostRespose])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts
 
@router.post("/post", status_code=status.HTTP_201_CREATED, response_model=schemas.PostRespose)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/post/{id}", response_model=schemas.PostRespose)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found")
    return post
 
@router.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/post/{id}", status_code=status.HTTP_200_OK, response_model=schemas.PostRespose)
async def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    new_post = post_query.first()
    if new_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()