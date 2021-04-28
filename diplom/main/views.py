# response generate
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# views
from django.views import View

# our forms
from .forms import Register

# our models
from pprint import pprint
import json


# --------------------------------AUTH--------------------------------

@method_decorator(csrf_exempt, name='dispatch')
class LoginFormView(View):
    def post(self, request):
        user = authenticate(request, **request.POST.dict())
        print(user)
        if user is not None:
            login(request, user)

            return HttpResponseRedirect('/workplace')
        else:
            return HttpResponseRedirect('/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


@method_decorator(csrf_exempt, name='dispatch')
class RegisterFormView(View):
    context = {'form': Register()}

    def get(self, request):
        return render(request, 'helpers/register.html', self.context)

    def post(self, request):
        form = Register(request.POST)
        print(form)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
        return HttpResponseRedirect('/')


# --------------------------------INDEX--------------------------------


@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    context = {}

    def get(self, request):
        return render(request, 'index.html', context=self.context)


# --------------------------------PAGES--------------------------------

@method_decorator(csrf_exempt, name='dispatch')
class DragAndDrop(View):
    def post(self, request):
        print(json.loads(request.body))
        # print(request.body)
        return HttpResponseRedirect('/index')


@method_decorator(csrf_exempt, name='dispatch')
class Workplace(View):
    context = {}

    def get(self, request):
        self.context['username'] = request.user.username
        return render(request, 'workplace.html', context=self.context)


@method_decorator(csrf_exempt, name='dispatch')
class HomePage(View):

    def get(self, request):
        render(request, 'pages/home.html')


@method_decorator(csrf_exempt, name='dispatch')
class DealsPage(View):

    def get(self, request):
        render(request, 'pages/home.html')


@method_decorator(csrf_exempt, name='dispatch')
class TasksPage(View):

    def get(self, request):
        render(request, 'pages/home.html')


@method_decorator(csrf_exempt, name='dispatch')
class ClienstsPage(View):

    def get(self, request):
        render(request, 'pages/home.html')


@method_decorator(csrf_exempt, name='dispatch')
class AnalyticsPage(View):

    def get(self, request):
        render(request, 'pages/home.html')

# --------------------------------SOME--------------------------------
