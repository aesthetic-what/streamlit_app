from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import *
from db import get_session


router = APIRouter(prefix="/user")

@router.get("/get_users")
async def get_users():
    ...


@router.post("/register")
async def register(username: str, password: str, email: str | None,
                   session: Annotated[AsyncSession, Depends(get_session)]):
    
    user = await session.scalar(select(User).where((User.username == username) | (User.email == email)))

    if not user:
        new_user = User(username=username, password=password, email=email)
        session.add(new_user)
        await session.commit()
        return {"status_code": "ok", "data": {
            "detail": "Вы успешно зарегистрировались"
        }}
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Такой пользователь уже есть")



@router.post("/login")
async def login(username: str, password: str,
                session: Annotated[AsyncSession, Depends(get_session)]):
    user = await session.scalar(select(User).where(User.username == username))
    # print(user.username, user.password)
    if user:
        if user.password == password and user.username:
            return {"status_code": "ok", "data": {
                "detail": "Вы успешно автоирзовались"
            }}
        elif user.password != password or user.username != username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Логин или пароль введен не правильно")

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Введите данные")