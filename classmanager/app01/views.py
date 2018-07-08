from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.

def test(requests):
    # A=models.Class.objects.get(id=1).student_set.all()
    # for row in A:
    #     print(row.name)
    #     print(row.cs.title)
    B=models.Class.objects.get(id=2).test.all()
    for row in B:
        print(row.name)
        print(row.cs.title)
    C=models.Class.objects.values("title","test__name")
    print(C)
    return HttpResponse("oK")

from functools import wraps

# def check_user(f):
#     @wraps(f)
#     def inner(request,*args,**kwargs):
#         if request.session.get("is_login")=="1":
#             return f(request,*args,**kwargs)
#         else:
#             return redirect('/index')
#     return inner
#
# def login(request):
#     if request.method=="GET":
#         return render(request,"login.html")
#     elif request.method=="POST":
#         user=request.POST.get("username")
#         pwd=request.POST.get("password")
#         user_obj=models.User.objects.filter(username=user,password=pwd).first()
#         user_id=user_obj.id
#         if user_obj:
#             request.session["is_login"]="1"
#             request.session["user_id"]=user_id
#             return redirect('/index')
#         return render(request,"login.html")
#
# @check_user
# def index(request):
#     userid=request.session.get("user_id")
#     print("userid:",userid)
#     user=models.User.objects.filter(id=userid).first()
#     if user:
#         return render(request,"index.html",{"user":user})
#     return redirect('/login')

#首先要创建超级用户：python manage.py createsuperuser
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        user=request.POST.get("username")
        pwd=request.POST.get("password")
        #判断用户名密码是否正确
        user=auth.authenticate(username=user,password=pwd)
        print(user)
        if user:
            # print(user.is_authenticated())#判断当前用户是否通过了认证
            auth.login(request,user) #将登陆的用户封装到request.user
            return redirect('/index')
        return render(request,"login.html")

@login_required  #需要在settings注册,如果未通过认证，http://127.0.0.1:8000/login/?next=/index会先跳到指定的页面
def index(request):
    user_name=request.user.username
    print("登陆用户:",user_name)
    # if not request.user.is_authenticated():
    #     return redirect('/login')
    return render(request,"index.html",{"username":user_name})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login')


def register(request):
    pass