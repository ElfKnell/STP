from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import CreateUserAPIView, UpdateUserAPIView


app_name = 'user'
urlpatterns = [
    path('user/create/', CreateUserAPIView.as_view()),
    path('user/obtain_token/', obtain_jwt_token),
    path('user/refresh_token/', refresh_jwt_token),
    path('user/detail/<int:pk>', UpdateUserAPIView.as_view()),
]