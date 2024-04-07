from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member


class MemberJoinView(View):
    def get(self,request):
        return render(request,'member/join.html')


class MemberCheckIdView(APIView):
    def get(self, request):
        member_id = request.GET['member_id']
        is_duplicated = Member.objects.filter(member_id=member_id).exists()
        return Response({'isDup':is_duplicated})





