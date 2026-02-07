from datetime import datetime
from typing import List

from django.core.paginator import Paginator
from ninja import Router, Schema

from order.models import Request

router = Router()


class RequestCreateSchema(Schema):
    student_name: str
    student_age: int
    student_gender: str
    student_grade: str

    subject: str
    experienced: bool

    method: str
    tutor_gender: str

    lesson_date: str
    lesson_time: str
    lesson_days: int

    payment_type: str
    salary: int


@router.post("/create")
def create_request(request, data: RequestCreateSchema):
    user = request.user
    Request.objects.create(
        parent=user,
        student_name=data.student_name,
        student_age=data.student_age,
        student_gender=data.student_gender,
        student_grade=data.student_grade,
        subject=data.subject,
        experienced=data.experienced,
        method=data.method,
        tutor_gender=data.tutor_gender,
        lesson_date=data.lesson_date,
        lesson_time=data.lesson_time,
        lesson_days=data.lesson_days,
        payment_type=data.payment_type,
        salary=data.salary,
    )
    return {"status": "success"}


class RequestSchema(Schema):
    id: int
    student_name: str
    student_age: int
    student_gender: str
    student_grade: str
    subject: str
    experienced: bool
    method: str
    tutor_gender: str
    lesson_date: str
    lesson_time: str
    lesson_days: int
    payment_type: str
    salary: int
    create_time: datetime


@router.get("/get", response=RequestSchema)
def get_request(request, id: int):
    return Request.objects.get(pk=id)


@router.get("/list", response=List[RequestSchema])
def get_list(request, page: int = 1, per_page: int = 8):
    pages = Paginator(Request.objects.all(), per_page)
    return pages.get_page(page)


@router.get("/list/id", response=List[int])
def get_id_list(request, page: int = 1, per_page: int = 8):
    pages = Paginator(Request.objects.values_list("id", flat=True), per_page)
    return pages.get_page(page)


@router.get('/list/page', response=int)
def get_list_page(request, page: int = 1, per_page: int = 8):
    pages = Paginator(Request.objects.all(), per_page)
    return pages.num_pages
