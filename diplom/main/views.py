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

# other libs
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


# --------------------------------WORKPLACE--------------------------------


@method_decorator(csrf_exempt, name='dispatch')
class Workplace(View):
    context = {}

    def get(self, request):
        self.context['username'] = request.user.username
        return render(request, 'workplace.html', context=self.context)


# --------------------------------HOME_DRAG--------------------------------

@method_decorator(csrf_exempt, name='dispatch')
class DragAndDrop(View):
    def post(self, request):
        print(json.loads(request.body))
        # print(request.body)
        return HttpResponseRedirect('/workplace')


@method_decorator(csrf_exempt, name='dispatch')
class HomePage(View):
    def get(self, request):
        return render(request, 'pages/home.html')


# --------------------------------OTHER_PAGE--------------------------------

@method_decorator(csrf_exempt, name='dispatch')
class CasesPage(View):
    context = {}

    def get(self, request):
        self.context['form'] = []
        return render(request, 'pages/cases.html', context=self.context)


@method_decorator(csrf_exempt, name='dispatch')
class TasksPage(View):
    context = {}

    def get(self, request):
        self.context['form'] = []
        return render(request, 'pages/tasks.html', context=self.context)


@method_decorator(csrf_exempt, name='dispatch')
class ClienstsPage(View):
    context = {}

    def get(self, request):
        self.context['form'] = []
        return render(request, 'pages/clients.html', context=self.context)


# --------------------------------ADDING_EDITING_ON_PAGES-----------------------------

@method_decorator(csrf_exempt, name='dispatch')
class Add_Elem(View):
    content = {}

    def post(self, request):
        print(json.loads(request.body))
        # print(request.body)
        return HttpResponseRedirect('/index')

    def get(self, request, page):
        if page == 'deals':
            self.content['form'] = []
            return render(request, 'add/deal.html')
        elif page == 'tasks':
            self.content['form'] = []
            return render(request, 'add/task.html')
        elif page == 'clients':
            self.content['form'] = []
            return render(request, 'add/client.html')


# --------------------------------ANAL_SETTINGS-----------------------------

@method_decorator(csrf_exempt, name='dispatch')
class AnalyticsPage(View):
    def get(self, request):
        return render(request, 'pages/analytics.html')


@method_decorator(csrf_exempt, name='dispatch')
class SettingsPage(View):
    def get(self, request):
        return render(request, 'pages/settings.html')
