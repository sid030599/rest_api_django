from django.urls import path
from .views import Record, Login, Logout, Users

urlpatterns = [

    path('User/', Users.as_view(), name="reg"),
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),

]
