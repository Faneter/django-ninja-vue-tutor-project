from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import Field


class UserType(models.TextChoices):
    UNKNOWN = "U", "未认证"
    TUTOR = "T", "家教"
    PARENT = "P", "家长"


class User(AbstractUser):
    phone = models.CharField(
        "手机号",
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(regex=r"^1[3-9]\d{9}$", message="请输入有效的手机号")
        ],
    )

    # type = models.CharField("用户类型", max_length=1, choices=UserType, default=UserType.UNKNOWN)

    @property
    def type(self):
        parent = getattr(self, 'parent', None)
        if parent and self.parent.status == VerificationStatus.PASSED:
            return UserType.PARENT
        else:
            return UserType.UNKNOWN

    USERNAME_FIELD = 'phone'


class VerificationStatus(models.TextChoices):
    WAITING = "W", "待审核"
    PASSED = "P", "审核通过"
    FAILED = "F", "审核不通过"


class ParentVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="parent")
    id_card = models.CharField("身份证", max_length=18, default="")
    status = models.CharField("审核状态", max_length=1, choices=VerificationStatus, default=VerificationStatus.WAITING)
