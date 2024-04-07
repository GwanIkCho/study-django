"""
URL configuration for view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main.views import MainView
from view.views import UserNameFormView, UserNameView, UserResultView, NumberInpotFormView, NumberInpotView, \
    NumberResultView, TextInputFormView, TextInputView, TextResultView, EventInputFormView, EventInputView, \
    EventResultView, NumInputFormView, NumInputView, NumResultView

# from view.views import StudentRegisterView, StudentResultView, StudentRegisterFormView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('post/', include('post.urls')),
    path('product/', include('product.urls')),
    # path('student/register/form/', StudentRegisterFormView.as_view(), name='student-register-form'),
    # path('student/register/', StudentRegisterView.as_view(), name='student-register'),
    # path('student/result/', StudentResultView.as_view(), name='student-result'),
    # path('member/register/form/', MemberNameFormView.as_view(), name='name-form'),
    # path('member/register/', MemberNameView.as_view(), name='name'),
    # path('member/result/', MemberNameResultView.as_view(), name='name-result'),
    path('user/register/form/', UserNameFormView.as_view(), name='user-form'),
    path('user/register/', UserNameView.as_view(), name='user'),
    path('user/result/', UserResultView.as_view(), name='user-result'),
    path('number/input/form/', NumberInpotFormView.as_view(), name='number-form'),
    path('number/input/', NumberInpotView.as_view(), name='number'),
    path('number/result/', NumberResultView.as_view(), name='number-result'),
    path('text/input/form/', TextInputFormView.as_view(), name='text-form'),
    path('text/input/', TextInputView.as_view(), name='text'),
    path('text/result/', TextResultView.as_view(), name='text-result'),
    path('event/input/form/', EventInputFormView.as_view(), name='event-form'),
    path('event/input/', EventInputView.as_view(), name='event'),
    path('event/result/', EventResultView.as_view(), name='event-result'),
    path('num/input/form/', NumInputFormView.as_view(), name='num-form'),
    path('num/input/', NumInputView.as_view(), name='num'),
    path('num/result/', NumResultView.as_view(), name='num-result'),
    path('', MainView.as_view(), name='main')


]













