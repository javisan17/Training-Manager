from django.contrib import admin
from django.urls import path
from .views import VRegister, my_logout, VLogin


urlpatterns = [
    path('register/', view=VRegister.as_view(), name="register"),
    path('logout/', view=my_logout, name="logout"),
    path('login/', view=VLogin.as_view(), name="login"),
]