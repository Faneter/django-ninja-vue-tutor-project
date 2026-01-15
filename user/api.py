from django.contrib import auth

from ninja import Router, Schema
from ninja.security import django_auth

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
    user.save()


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


@router.get("/test")
def test(request):
    if request.user.is_authenticated:
        return {"message": f"Hello, {request.user.username}"}
    else:
        return {"message": "Not logged in."}


@router.get("/test_auth", auth=django_auth)
def test_auth(request):
    return {"message": f"Hello, {request.user.username}"}
