
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main.views import MainView
from post.views import PostWriteView, PostDetailView, PostUpdateView, PostDeleteView, PostListView, PostListAPI

app_name = 'post'

urlpatterns = [
    path('write/',PostWriteView.as_view(),name='write'),
    path('detail/',PostDetailView.as_view(), name='detail'),
    path('update/<int:post_id>/',PostUpdateView.as_view(), name='update'),
    path('delete/<int:post_id>/', PostDeleteView.as_view(), name='delete'),
    path('list/', PostListView.as_view(), name='list'),
    path('list/<int:page>/', PostListAPI.as_view(), name='list-api')
]









