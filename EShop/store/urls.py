from django.urls import path, include
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import Order
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', CheckOut.as_view(), name='checkout'),
    path('orders/', auth_middleware(Order.as_view()), name='orders'),
]
