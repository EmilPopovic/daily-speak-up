from fastapi import APIRouter, FastAPI, File, UploadFile, HTTPException, Depends, status, Security
from ..deps import get_auth_service
from ...models import User
from ...schemas import UsernameData, EmailData, InterestData, JWTPayload
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from ...db import get_db
from fastapi.responses import JSONResponse 


router = APIRouter(prefix="/userdata", tags=["UserData"])

@router.post("/name", response_class=JSONResponse)
async def set_username(
   username_data: UsernameData,
   db: Session = Depends(get_db),
   auth_result: JWTPayload = Security(get_auth_service().verify)
):
   auth0_user_id = auth_result['sub']
   
   user: User | None = db.query(User).filter(
      User.auth0_user_id == auth0_user_id
   ).first()

   if user is None:
      raise HTTPException(
         status_code=status.HTTP_404_NOT_FOUND, 
         detail="User not found"
      ) 
   
   existing_user: User | None = db.query(User).filter(
      User.handle == username_data.username, 
      User.id != user.id
   ).first()

   if existing_user:
      raise HTTPException(
         status_code=status.HTTP_409_CONFLICT, 
         detail="Username already taken"
      )
   
   user.handle = username_data.username
   db.commit()
   db.refresh(user)

   return JSONResponse(
            content = {
               "message": "Username updated successfully", 
               'username': username_data.username
            }
   )

@router.post("/email", response_class=JSONResponse)
async def set_email(
   email_data: EmailData,
   db: Session = Depends(get_db),
   auth_result: JWTPayload = Security(get_auth_service().verify)
):
   auth0_user_id = auth_result['sub']

   user: User | None = db.query(User).filter(
      User.auth0_user_id == auth0_user_id
   ).first()

   if user is None:
      raise HTTPException(
         status_code=status.HTTP_404_NOT_FOUND, 
         detail="User not found"
      ) 
   
   user.email = email_data.email

   db.commit()
   db.refresh(user)
   return JSONResponse(
      content={
         "message": "Email updated successfully", 
         'email': email_data.email
      }
   )