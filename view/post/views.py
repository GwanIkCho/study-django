from django.db import transaction
from django.db.models import F
from django.db.models.functions import math
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlparse.utils import offset

from member.models import Member
from post.models import Post, PostFile
from post.serializers import PostSerializer


class PostWriteView(View):
    def get(self, request):
        return render(request, 'post/write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        file = request.FILES

        member = Member(**request.session['member'])

        data = {
            'post_title': data['post-title'],
            'post_content': data['post-content'],
            'member': member
        }
        post = Post.objects.create(**data)

        for key in file:
            PostFile.objects.create(post= post,path=file[key])

        return redirect(post.get_absolute_url())


class PostDetailView(View):
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])

        post.post_view_count += 1
        post.save(update_fields=['post_view_count'])

        context = {
            'post': post
        }
        return render(request, 'post/detail.html', context)




class PostUpdateView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        context = {
            'post' : post
        }
        return render(request, 'post/update.html', context)


    @transaction.atomic
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        data = request.POST
        post.post_title = data['post-title']
        post.post_content = data['post-content']
        post.save(update_fields=['post_title', 'post_content'])

        return redirect(post.get_absolute_url())



class PostDeleteView(View):
    def get(self, request):
        Post.objects.filter(id=request.GET['id']).update(status=False)

        # 나중에 이동하는 곳으로 적기
        return redirect('/post/list')


class PostListView(View):
    def get(self, request):
        return render(request, 'post/list.html')


class PostListAPI(APIView):
    def get(self, request, page):
        row_count = 5

        offset = (page - 1) * row_count
        limit = page * row_count
        columns = [
            'id',
            'post_title',
            'post_content',
            'post_view_count',
            'member_name'
        ]
        posts = Post.objects\
                    .annotate(member_name=F('member__member_name'))\
                    .values(*columns)[offset:limit]

        total_count = Post.objects.count() # 전체 포스트 개수

        post_info = {
            'posts': posts,
            'totalCount': total_count
        }

        return Response(post_info)