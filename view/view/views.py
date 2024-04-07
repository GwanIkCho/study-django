# 학생의 번호, 국어, 영어, 수학 점수를 전달받은 뒤
# 총점과 평균을 화면에 출력한다.
from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


class UserNameFormView(View):
    def get(self, request):
        return render(request, 'task/user/register.html')

class UserNameView(View):
    def get(self, request):
        data = request.GET
        name = data['user-name']
        age = data['user-age']

        return redirect(f'/user/result?name={name}&age={age}')

class UserResultView(View):
    def get(self, request):
        data = request.GET
        asd = []
        if int(data['age']) >20:
            asd.append(f'{data["name"]} 님의 나이는 늙')
        else:
            asd.append(f'{data["name"]}님의 나이는 어린')


        return render(request, 'task/user/result.html', {'asd':asd})


class NumberInpotFormView(View):
    def get(self, request):
        return render(request, 'task/number/input.html')

class NumberInpotView(View):
    def get(self, request):
        number = int(request.GET.get('number'))

        return redirect( f'/number/result?number={number}')

class NumberResultView(View):
    def get(self,request):
        number = int(request.GET.get('number'))
        random_number = randint(1, 10)
        asd = []
        if number == random_number:
            asd.append('축하드립니다! 당첨입니다!')
        else:
            asd.append(f'{abs(random_number)-abs(number)}만큼 차이납니다!')


        return render(request, 'task/number/result.html', {'asd': asd})

class TextInputFormView(View):
    def get(self, request):
        return render(request, 'task/text/input.html')

class TextInputView(View):
    def get(self, request):
        text = request.GET.get('text')
        return redirect( f'/text/result?text={text}')

class TextResultView(View):
    def get(self,request):
        text = request.GET.get('text')
        want_text = text.swapcase
        return render(request, 'task/text/result.html', {'want_text':want_text})

class EventInputFormView(View):
    def get(self, request):
        return render(request, 'task/event/register.html')

class EventInputView(View):
    def get(self, request):
        name = request.GET.get('event-name')
        title = request.GET.get('event-title')
        content = request.GET.get('event-content')

        return redirect(f'/event/result?name={name}&title={title}&content={content}')

class EventResultView(View):
    def get(self,request):
        data = request.GET
        context ={
            'name': data['name'],
            'title' : data['title'],
            'content' : data['content']
        }
        print(context)
        print(1)
        return render(request, 'task/event/result.html', {'context':context})


class NumInputFormView(View):
    def get(self, request):
        return render(request, 'task/num/input.html')

class NumInputView(View):
    def get(self, request):
        number = request.GET.get('number')
        return redirect(f'/num/result?number={number}')


class NumResultView(View):
    def get(self, request):
        numbers = request.GET['number']
        result= []
        if numbers is None:
            print("입력값이 없습니다.")
            result.append('입력값이 없습니다.')
        else:
            print("입력값이 있습니다.")
            num_count = len(numbers)
            result.append(f'입력하신 값은 {numbers} 이며, {num_count} 자리수입니다.')

        return render(request, 'task/num/result.html', {'result':result})


# 상품정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST방식으로 설계한 뒤
# 화면에 출력하기
# ex)
# product/1
# task/product/product.html



