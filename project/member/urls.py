
from django.contrib import admin
from django.urls import path, include

from member.views import MemberJoinView, MemberCheckIdView

app_name = 'member'

urlpatterns = [
    path('join/',MemberJoinView.as_view(), name='join'),
    path('check-id',MemberCheckIdView.as_view(), name='check-id')

]


