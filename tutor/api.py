from ninja import NinjaAPI
from user.api import router as UserRouter

api = NinjaAPI()

api.add_router("/user/", UserRouter)


@api.get("/hello")
def hello(request):
    return "Hello World!"
