from django.contrib import auth
from django.db import IntegrityError

from ninja import Router, Schema, File, Form
from ninja.files import UploadedFile

from .models import User, ParentVerification, VerificationStatus, UserType, TutorVerification

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
        return {"status": "success", "message": "已提交审核。"}
    else:
        if verification.status == VerificationStatus.WAITING:
            return {"status": "failed", "error_message": "认证已提交审核，请不要重复提交。"}
        elif verification.status == VerificationStatus.PASSED:
            return {"status": "failed", "error_message": "此账号已认证，请不要重复提交。"}
        elif verification.status == VerificationStatus.FAILED:
            verification.id_card = data.id_card
            verification.status = VerificationStatus.WAITING
            verification.save()
            return {"status": "success", "message": "已提交审核。"}
        else:
            return {"status": "false", "error_message": "未知错误。"}


class TutorVerificationSchema(Schema):
    id_card: str
    college_entrance_score: int


@router.post("/verify/tutor")
def verify_tutor(
        request,
        data: TutorVerificationSchema = Form(...),
        student_card: UploadedFile = File(...),
        teacher_qualification_certificate: UploadedFile = File(None)
):
    user = request.user
    verification = TutorVerification.objects.filter(user=user).first()
    if verification is None:
        TutorVerification.objects.create(
            user=user,
            id_card=data.id_card,
            student_card=student_card,
            college_entrance_score=data.college_entrance_score,
            teacher_qualification_certificate=teacher_qualification_certificate,
            status=VerificationStatus.WAITING
        )
        return {"status": "success", "message": "已提交审核。"}
    else:
        if verification.status == VerificationStatus.WAITING:
            return {"status": "failed", "error_message": "认证已提交审核，请不要重复提交。"}
        elif verification.status == VerificationStatus.PASSED:
            return {"status": "failed", "error_message": "此账号已认证，请不要重复提交。"}
        elif verification.status == VerificationStatus.FAILED:
            verification.id_card = data.id_card
            verification.student_card = student_card
            verification.college_entrance_score = data.college_entrance_score
            verification.teacher_qualification_certificate = teacher_qualification_certificate
            verification.status = VerificationStatus.WAITING
            verification.save()
            return {"status": "success", "message": "已提交审核。"}
        else:
            return {"status": "false", "error_message": "未知错误。"}


class UserVerificationStatusSchema(Schema):
    status: str
    """
    具体的验证状态值
     - "NONE": 未认证
     - "WAITING": "已提交但尚未审核"
     - "FAILED": "提交了但审核失败了"
     - "PARENT": "认证为了家长"
     - "TUTOR": "认证为了学生"
    """


@router.get("/verify/status", response=UserVerificationStatusSchema)
def get_user_verification_status(request):
    user = request.user
    if user.type == UserType.PARENT:
        return {"status": "PARENT"}
    elif user.type == UserType.TUTOR:
        return {"status": "TUTOR"}
    else:
        parent = getattr(user, 'parent', None)
        tutor = getattr(user, 'tutor', None)
        if parent and tutor:
            if parent.status == VerificationStatus.WAITING or tutor.status == VerificationStatus.WAITING:
                return {"status": "WAITING"}
            elif parent.status == VerificationStatus.FAILED and tutor.status == VerificationStatus.FAILED:
                return {"status": "FAILED"}
            else:
                return {"status": "FAILED"}
        elif parent:
            if parent.status == VerificationStatus.WAITING:
                return {"status": "WAITING"}
            elif parent.status == VerificationStatus.FAILED:
                return {"status": "FAILED"}
            else:
                return {"status": "FAILED"}
        elif tutor:
            if tutor.status == VerificationStatus.WAITING:
                return {"status": "WAITING"}
            elif tutor.status == VerificationStatus.FAILED:
                return {"status": "FAILED"}
            else:
                return {"status": "FAILED"}
        else:
            return {"status": "FAILED"}


class UserInformationSchema(Schema):
    phone: str
    username: str
    type: str


@router.get("/information", response=UserInformationSchema)
def get_user_information(request):
    return request.user
