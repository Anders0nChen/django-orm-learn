from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from utils.mypage import Page
from functools import wraps
# Create your views here.
def hello(request):

    return HttpResponse("hello")


def person(request):
    # 从url取页数
    try:
        page_num = int(request.GET.get("page"))
    except Exception as e:
        page_num = 1

    # per page num
    per_page = 10


    # calculate page number
    total_person = models.Person.objects.all().count()
    total_page, m = divmod(total_person, per_page)
    if m: total_page += 1
    if page_num > total_page:page_num = total_page

    data_start = (page_num - 1) * 10
    data_end = page_num * 10

    # max page number
    max_page = 11
    # if total_page <= max_page or page_num < max_page // 2:
    #     page_start=0
    #     page_end=max_page
    # else:
    #     half_max_page = max_page // 2
    #     page_start = page_num - half_max_page
    #     page_end = page_num + half_max_page

    half_max_page = max_page // 2
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page

    if page_start <= 1:
        page_start = 1
        page_end = max_page

    if page_end > total_page:
        page_end = total_page
        page_start = total_page - max_page + 1

    all_person = models.Person.objects.all()[data_start:data_end]

    # concat html seperate code
    html_list = []
    html_list.append('<li><a href="/person/?page=1">第一页</a></li>')
    if page_num <= 1:
        html_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    else:
        html_list.append('<li><a href="/person/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))

    for i in range(page_start, page_end + 1):
        if i == page_num:
            tmp = '<li class="active"><a href="/person/?page={0}">{0}</a></li>'.format(i)
        else:
            tmp = '<li><a href="/person/?page={0}">{0}</a></li>'.format(i)
        html_list.append(tmp)

    if page_num >= total_page:
        html_list.append('<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        html_list.append('<li><a href="/person/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num+1))

    html_list.append('<li><a href="/person/?page={}">尾页</a></li>'.format(total_page))
    page_html = "".join(html_list)
    return render(request, "person.html", {"person":all_person, "page_html":page_html})

def depts(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    total_count = models.Dept.objects.all().count()
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/depts/", max_page=11,)
    print(page_obj.start, page_obj.end)
    ret = models.Dept.objects.all().order_by("id")[page_obj.start:page_obj.end]
    print(ret)
    page_html = page_obj.page_html()
    return render(request, "depts.html", {"depts":ret, "page_html":page_html})

def check_login(func):
    @wraps(func) # 保留原有函数的名称和docstring
    def wrapper(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default='0', salt="salt")
        if ret == "1":
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            print(next_url)
            return redirect("/login/?next={}".format(next_url))
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
                rep = redirect("/home/")
            # rep.set_cookie("is_login",1)
            rep.set_signed_cookie("is_login", "1", salt="salt", max_age=60) # 单位：s
            return rep
        else:
            error_msg = "用户名或密码错误"
    return render(request, "login.html", {"msg":error_msg})

@check_login
def home(request):
    # ret = request.COOKIES.get("is_login", 0)
    # ret = request.get_signed_cookie("is_login", default='0', salt="verydifficultstrings")
    # if ret == '1':
        return render(request, "home.html")
    # else:
    #     return redirect("/login/")

@check_login
def index(request):
    return render(request, "index.html")


@check_login
def logout(request):
    rep = redirect("/login/")
    rep.delete_cookie("is_login")
    return rep