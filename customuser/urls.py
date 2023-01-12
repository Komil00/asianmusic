from django.urls import path, include
from .views import UsersViewList, UsersVerifyApiView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'', UsersViewSet)
urlpatterns = [
    path('all_users', UsersViewList.as_view()),
    path('verify', UsersVerifyApiView.as_view())
]


