from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router = APIRouter(tags=["Authentication"])

@router.post('/login')
async def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.http_404, detail={f"Invalid Credentials"})
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.http_404, detail={f"Invalid Credentials"})
    return {"data": "success"} 
