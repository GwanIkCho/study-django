from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        try:
            member = request.session['member']
        except:
            member = None
        return render(request, 'main/main.html', {'member': member})