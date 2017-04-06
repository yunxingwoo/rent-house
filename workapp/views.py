from django.shortcuts import render, redirect, Http404, HttpResponse
from workapp.models import Area, HouseInfo, UserInfo, Collect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

from workapp.forms import UserForm,LoginForm,ModifyUserForm
from django.contrib.auth import login as auth_login
# Create your views here.


def index(request):
    context={}
    area = Area.objects.all()
    context['area'] = area
    return render(request, 'index.html', context)

def list(request):
    context={}
    #if request.Method == "GET":
    house_lists = HouseInfo.objects.all();
    house_sum = len(house_lists)

    print(house_lists)
    for house_list in house_lists:
        print(house_list.rent)

    page_robot = Paginator(house_lists, 9)
    page_num = request.GET.get('page')
    try:
        house_lists = page_robot.page(page_num)
    except EmptyPage:
        house_lists = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        house_lists = page_robot.page(1)
    context['house_lists'] = house_lists
    context['house_sum'] = house_sum
    return render(request, 'list.html', context)

def detail(request,id):
    context={}
    installations_lists = []
    house_lists =[]
    house_address = []
    house_info = HouseInfo.objects.get(id=id)
    for j in house_info.house.split():
        house_lists.append(j)
    #print(house_info.title)
    for k in house_info.address.split(" "):
        house_address.append(k)
    for i in house_info.installations.split(" "):
        installations_lists.append(i)
    context['house_info'] = house_info
    context['installations_lists'] = installations_lists
    context['house_lists'] = house_lists
    context['house_address'] = house_address
    return render(request, 'detail.html', context)

def userinfo(request):
    context={}
    return render(request, 'personcenter.html', context)

def login(request):
    if request.method == "GET":
        loginform = LoginForm()
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            #email = request.POST['email']
            print("====email====")
            #print(username)
            email = loginform.cleaned_data['email']
            passwords = loginform.cleaned_data['password']
            user = User.objects.get(email=email)
            username = user.username
            user = authenticate(username=username, password=passwords)
            print("====user====")
            print(user)
            if user is not None:
                auth_login(request,user) #<====记住这里要用auth_login
                return redirect(to='index')
            else:
                return redirect(to='login')
    # if request.method == "GET":
    #     form = AuthenticationForm

    # if request.method == "POST":
    #     form = AuthenticationForm(data=request.POST)
    #     print(form)
    #     if form.is_valid():
    #         auth_login(request,form.get_user())
    #         return redirect(to="index")

    context={}
    context['form'] = loginform
    print("========a=========")
    print(loginform)
    return render(request, 'login.html', context)

def register(request):
    if request.method == "GET":
        userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        form = UserCreationForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            user_id = request.user.id #取得用户id
           # user = User() #把user模型赋值给user
           # user.username = username #赋值用户名
            #user.set_password(password) #赋值密码
            #user.email=email #赋值邮件地址.User模型里有email字段
            #user.save() #保存增加
            User.objects.create_user(username=username,email=email,password=password)
            c = UserInfo(email=email,username=username,password=password)
            c.save()

            return redirect(to='login')

    context={}
    context['form'] = userform
    return render(request, 'register.html', context)

def alteruser(request):
    if request.method == "GET":
        alteruserform = ModifyUserForm()
    if request.method == "POST":
        alteruserform = ModifyUserForm(request.POST)
        if alteruserform.is_valid():
            username = alteruserform.cleaned_data['username']
            password = alteruserform.cleaned_data['password']
            user_id = request.user.id
            user_name = request.user.username
            user = User.objects.get(username=user_name)
            user.set_password(password)
            user.save()
            #UserInfo.objects.filter(user_belong_to_id=user_id).update(username=username)
            return render(request,'personmodify.html')
    context={}
    context['form'] =  alteruserform
    return render(request, 'personmodify.html', context)

def appointment(request):
    context={}
    return render(request, 'appointment.html', context)
