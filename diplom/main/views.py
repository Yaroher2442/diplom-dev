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
from .forms import Register, CasesAdd, ClientAdd, TaskAdd, FunnelAdd

# our models
from .models import Cases, Clients, Tasks, Funnels
from django.contrib.auth import get_user_model
# other libs
from pprint import pprint
import json
from datetime import datetime
from django.utils import timezone


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
        from django.contrib.auth import get_user_model
        self.context['username'] = request.user.username
        self.context['form'] = FunnelAdd()
        return render(request, 'workplace.html', context=self.context)


# --------------------------------HOME_DRAG--------------------------------

@method_decorator(csrf_exempt, name='dispatch')
class DragAndDrop(View):
    def post(self, request):
        js_data = json.loads(request.body)
        for case in Cases.objects.filter(funnel=Funnels.objects.get(id=str(js_data['container'].split('-')[1]))):
            if case.f_position >= js_data['index']:
                case.f_position += 1
                case.save()
        case = Cases.objects.get(id=int(js_data['elem'].split('-')[1]))
        case.funnel = Funnels.objects.get(id=str(js_data['container'].split('-')[1]))
        case.f_position = js_data['index']
        case.save()
        return HttpResponseRedirect('/workplace')


@method_decorator(csrf_exempt, name='dispatch')
class HomePage(View):
    context = {}

    def get(self, request):
        self.context['form'] = FunnelAdd()
        funs_cases = {}
        for funn in Funnels.objects.all():
            if funn.name not in funs_cases.keys():
                funs_cases[funn] = Cases.objects.filter(funnel=funn.id).order_by('f_position')
        print(funs_cases)
        self.context['drop_js_string'] = ','.join([".droppable-area" + str(i.id) for i in funs_cases.keys()])
        self.context['data'] = funs_cases
        return render(request, 'pages/home.html', context=self.context)


# --------------------------------OTHER_PAGE--------------------------------

@method_decorator(csrf_exempt, name='dispatch')
class CasesPage(View):
    context = {}

    def get(self, request):
        self.context['form'] = CasesAdd()
        self.context['data'] = Cases.objects.all()
        return render(request, 'pages/cases.html', context=self.context)


@method_decorator(csrf_exempt, name='dispatch')
class TasksPage(View):
    context = {}
    True_colour_dict = {'Done': "green", 'Wait': 'yellow', 'Created': 'blue'}
    False_colour_dict = {'Stop': 'purlpe', 'Canceled': 'black'}

    def get(self, request):
        self.context['form'] = TaskAdd()
        self.context['data'] = Tasks.objects.all()
        return render(request, 'pages/tasks.html', context=self.context)


@method_decorator(csrf_exempt, name='dispatch')
class ClienstsPage(View):
    context = {}

    def get(self, request):
        self.context['form'] = ClientAdd()
        self.context['data'] = Clients.objects.all()
        return render(request, 'pages/clients.html', context=self.context)


# --------------------------------ADDING_EDITING_DELITE_ON_PAGES-----------------------------

@method_decorator(csrf_exempt, name='dispatch')
class Add_Elem(View):
    content = {}

    def post(self, request, page):
        if page == 'case':
            form = CasesAdd(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                for funn in Cases.objects.filter(funnel=Funnels.objects.get(id=1)):
                    funn.f_position += 1
                    funn.save()
                new_case = Cases(f_position=0,
                                 funnel_id=Funnels.objects.get(id=1).id,
                                 name=form.cleaned_data['name'],
                                 descr=form.cleaned_data['descr'],
                                 client=form.cleaned_data['client'],
                                 executor=form.cleaned_data['executor'],
                                 stage=Funnels.objects.get(id=1).name,
                                 owner=request.user.username,
                                 create_time=timezone.now(),
                                 change_time=timezone.now())
                new_case.save()
        elif page == 'task':
            form = TaskAdd(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                new_task = Tasks(name=form.cleaned_data['name'],
                                 case=form.cleaned_data['case'],
                                 descr=form.cleaned_data['descr'],
                                 create_time=timezone.now(),
                                 change_time=timezone.now(),
                                 status=form.cleaned_data['status']
                                 )
                new_task.save()
        elif page == 'client':
            form = ClientAdd(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                funnel = Funnels.objects.all()[0]
                new_client = Clients(**form.cleaned_data, funnel=funnel,
                                     create_time=timezone.now(),
                                     change_time=timezone.now())
                new_client.save()
        elif page == 'funnel':
            form = FunnelAdd(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                new_funnel = Funnels(**form.cleaned_data)
                new_funnel.save()
                # new_funnel.save()
        return HttpResponseRedirect('/workplace')


@method_decorator(csrf_exempt, name='dispatch')
class Change_Elem(View):
    content = {}

    def post(self, request, page, el_id):
        if page == 'case':
            case = Cases.objects.get(id=el_id)
            case.name = request.POST.get('name')
            case.descr = request.POST.get('descr')
            case.save()
        elif page == 'task':
            client = Tasks.objects.get(id=el_id)
            client.status = request.POST.get('status')
            client.descr = request.POST.get('descr')
            client.save()
        elif page == 'client':
            client = Clients.objects.get(id=el_id)
            client.descr = request.POST.get('descr')
            client.save()
        return HttpResponseRedirect('/workplace')


@method_decorator(csrf_exempt, name='dispatch')
class Delite_Elem(View):
    pass


# --------------------------------ANAL_SETTINGS-----------------------------

@method_decorator(csrf_exempt, name='dispatch')
class AnalyticsPage(View):
    def get(self, request):
        return render(request, 'pages/analytics.html')


@method_decorator(csrf_exempt, name='dispatch')
class SettingsPage(View):
    def get(self, request):
        return render(request, 'pages/settings.html')
