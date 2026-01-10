from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


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

    type = models.CharField("用户类型", max_length=1, choices=UserType, default=UserType.UNKNOWN)

    USERNAME_FIELD = 'phone'
