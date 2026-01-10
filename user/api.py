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
