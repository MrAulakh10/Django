from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    # path('',views.HomeView.as_view(),name='home'),
    # path('login',views.LoginInterfaceView.as_view(),name='login'),
    # path('logout',views.LogoutInterfaceView.as_view(),name='logout'),
    # path('register',views.SignupView.as_view(),name='register'),
    path('',views.getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
