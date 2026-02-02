from django.db import models
from django.db.models.enums import TextChoices
from django.utils import timezone

from user.models import User


class Gender(TextChoices):
    MALE = "M", "男"
    FEMALE = "F", "女"
    UNKNOWN = "U", "未知"


class Grade(TextChoices):
    PRIMARY_1 = "P1", "一年级"
    PRIMARY_2 = "P2", "二年级"
    PRIMARY_3 = "P3", "三年级"
    PRIMARY_4 = "P4", "四年级"
    PRIMARY_5 = "P5", "五年级"
    PRIMARY_6 = "P6", "六年级"
    JUNIOR_1 = "J1", "初一"
    JUNIOR_2 = "J2", "初二"
    JUNIOR_3 = "J3", "初三"
    SENIOR_1 = "S1", "高一"
    SENIOR_2 = "S2", "高二"
    SENIOR_3 = "S3", "高三"


class Subject(TextChoices):
    CHINESE = "CHI", "语文"
    MATH = "MAT", "数学"
    ENGLISH = "ENG", "英语"
    PHYSICS = "PHI", "物理"
    CHEMISTRY = "CHE", "化学"
    BIOLOGY = "BIO", "生物"
    POLITICS = "POL", "政治"
    HISTORY = "HIS", "历史"
    GEOMETRY = "GEO", "地理"


class Method(TextChoices):
    TUTOR_PLACE = "T", "学员上门"
    STUDENT_PLACE = "S", "家教上门"
    ONLINE = "O", "线上辅导"


class PaymentType(TextChoices):
    BY_DAY = "D", "按天收费"
    BY_HOUR = "H", "按小时收费"
    BY_COUNSELING = "C", "面议"


class Request(models.Model):
    parent = models.ForeignKey(User, verbose_name='家长', on_delete=models.CASCADE, related_name='parent_requests')

    student_name = models.CharField("学员姓名", max_length=20, default="")
    student_age = models.IntegerField("学员年龄", default=0)
    student_gender = models.CharField("学员性别", max_length=1, choices=Gender, default=Gender.MALE)
    student_grade = models.CharField("学员年级", max_length=2, choices=Grade, default=Grade.PRIMARY_1)

    subject = models.CharField("辅导科目", max_length=3, choices=Subject, default=Subject.CHINESE)
    experienced = models.BooleanField("是否有基础", default=False)

    method = models.CharField("辅导方式", max_length=2, choices=Method, default=Method.ONLINE)
    tutor_gender = models.CharField("家教性别", max_length=1, choices=Gender, default=Gender.MALE)

    lesson_date = models.CharField("辅导日期", max_length=200, default="")
    lesson_time = models.CharField("单次辅导时间", max_length=200, default="")
    lesson_days = models.IntegerField("辅导天数", default=0)

    payment_type = models.CharField("支付方式", max_length=1, choices=PaymentType, default=PaymentType.BY_COUNSELING)
    salary = models.DecimalField("薪资", max_digits=10, decimal_places=2, default=0)

    create_time = models.DateTimeField("创建时间", default=timezone.now)


class Order(models.Model):
    request = models.ForeignKey(Request, verbose_name="要求", on_delete=models.CASCADE, related_name='orders')
    tutor = models.ForeignKey(User, verbose_name="家教", on_delete=models.CASCADE, related_name='tutor_orders')

    mark = models.IntegerField("评价", default=3)

    create_time = models.DateTimeField("创建时间", default=timezone.now)

    @property
    def parent(self):
        return self.request.parent
