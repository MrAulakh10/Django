# from typing import Any
# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# from datetime import datetime
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import LoginView,LogoutView
# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import redirect
# # Create your views here.


# class SignupView(CreateView):
#     form_class=UserCreationForm
#     template_name='home/register.html'
#     success_url='/smart/notes'

#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('notes.list')
#         return super().get(request, *args, **kwargs)

# class LogoutInterfaceView(LogoutView):
#     template_name='home/logout.html'

# class LoginInterfaceView(LoginView):
#     template_name='home/login.html'

# class HomeView(TemplateView):
#     template_name='home/welcome.html'
#     extra_context={'today':datetime.today()}
    
# class Authorized(LoginRequiredMixin,TemplateView):
#     template_name='home/authorized.html'
#     login_url='/admin'

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)