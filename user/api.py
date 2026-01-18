from django.contrib import auth
from django.db import IntegrityError

from ninja import Router, Schema

from .models import User

router = Router()


class RegisterSchema(Schema):
    phone: str
    username: str
    password: str


@router.post("/register")
def register(request, data: RegisterSchema):
    user = User(
        phone=data.phone,
        username=data.username,
    )
    user.set_password(data.password)
    try:
        user.save()
        return {"status": "success"}
    except IntegrityError:
        return {"status": "failed", "message": "手机号已注册。"}


class LoginSchema(Schema):
    phone: str
    password: str


@router.post("/login")
def login(request, data: LoginSchema):
    user = auth.authenticate(phone=data.phone, password=data.password)
    if user is not None:
        auth.login(request, user)
        return {"status": "success"}
    else:
        return {"status": "failed", "error_message": "账号或密码错误。"}


@router.post("/logout")
def logout(request):
    auth.logout(request)


@router.post("/is_logged_in")
def is_logged_in(request):
    if request.user.is_authenticated:
        return {"status": "true"}
    else:
        return {"status": "false"}
