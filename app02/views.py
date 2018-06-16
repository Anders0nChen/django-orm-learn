from django.shortcuts import render, HttpResponse, redirect
from django import views
from functools import wraps
# 将函数装饰器转变为类装饰器
from django.utils.decorators import method_decorator
# Create your views here.
# Session Version

def check_login(func):
    @wraps(func) # 保留原有函数的名称和docstring
    def wrapper(request, *args, **kwargs):
        ret = request.session.get("is_login")
        if ret == "1":
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            print(next_url)
            return redirect("/app02/login/?next={}".format(next_url))
    return wrapper

def login(request):
    print(request.get_full_path()) # 获取全路径
    print(request.path_info) # 获取路径
    print("login form path".center(80, '='))
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("pwd")
        next_url = request.GET.get("next")
        if user == "admin" and pwd == "123abc":
            if next_url:
                rep = redirect(next_url)
            else:
                rep = redirect("/app02/home/")
            request.session["is_login"] = "1"
            request.session["current_user"] = user
            return rep
        else:
            error_msg = "用户名或密码错误"
    return render(request, "app02/login.html", {"msg":error_msg})

@check_login
def home(request):
    # ret = request.COOKIES.get("is_login", 0)
    # ret = request.get_signed_cookie("is_login", default='0', salt="verydifficultstrings")
    # if ret == '1':
    user = request.session.get("current_user")
    return render(request, "app02/home.html", {"user":user})
    # else:
    #     return redirect("/login/")

@check_login
def index(request):
    return render(request, "app02/index.html")


@check_login
def logout(request):
    # rep.delete_cookie("is_login")
    request.session.flush()
    return redirect("/app02/login/")

# @method_decorator(check_login, name="get")
class UserInfo(views.View):
    @method_decorator(check_login)
    def get(self, request):
        return render(request, "app02/userinfo.html")