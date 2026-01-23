from ninja import NinjaAPI
from user.api import router as user_router
from order.api import router as order_router

api = NinjaAPI()

api.add_router("/user/", user_router)
api.add_router("/order/", order_router)
