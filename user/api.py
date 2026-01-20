from django.contrib import auth
from django.db import IntegrityError

from ninja import Router, Schema

from .models import User, ParentVerification, VerificationStatus

router = Router()


class RegisterSchema(Schema):
    phone: str
    username: str
    password: str


@router.post("/register", auth=None)
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


@router.post("/login", auth=None)
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


@router.post("/is_logged_in", auth=None)
def is_logged_in(request):
    if request.user.is_authenticated:
        return {"status": "true"}
    else:
        return {"status": "false"}


class ParentVerificationSchema(Schema):
    id_card: str


@router.post("/verify/parent")
def verify_parent(request, data: ParentVerificationSchema):
    user = request.user
    verification = ParentVerification.objects.filter(user=user).first()
    if verification is None:
        ParentVerification.objects.create(
            user=user,
            id_card=data.id_card,
            status=VerificationStatus.WAITING
        )
        return {"status": "true", "message": "已提交审核。"}
    else:
        if verification.status == VerificationStatus.WAITING:
            return {"status": "false", "message": "认证已提交审核，请不要重复提交。"}
        elif verification.status == VerificationStatus.PASSED:
            return {"status": "false", "message": "此账号已认证，请不要重复提交。"}
        elif verification.status == VerificationStatus.FAILED:
            verification.id_card = data.id_card
            verification.status = VerificationStatus.WAITING
            verification.save()
            return {"status": "true", "message": "已提交审核。"}
        else:
            return {"status": "false", "message": "未知错误。"}


class UserInformationSchema(Schema):
    phone: str
    username: str
    type: str


@router.get("/user/information", response=UserInformationSchema)
def get_user_information(request):
    return request.user
