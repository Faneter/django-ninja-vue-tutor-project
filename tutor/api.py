from ninja import NinjaAPI
from user.api import router as UserRouter

api = NinjaAPI()

api.add_router("/user/", UserRouter)
