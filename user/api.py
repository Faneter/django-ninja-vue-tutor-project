from django.contrib import auth

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
    user.save()


class LoginSchema(Schema):
    phone: str
    password: str


@router.post("/login")
def login(request, data: LoginSchema):
    user = auth.authenticate(phone=data.phone, password=data.password)
    if user is not None:
        auth.login(request, user)
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed."}


@router.post("/logout")
def logout(request):
    auth.logout(request)


@router.get("/test")
def test(request):
    if request.user.is_authenticated:
        return {"message": f"Hello, {request.user.username}"}
    else:
        return {"message": "Not logged in."}
