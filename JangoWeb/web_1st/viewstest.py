import json

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def setcookies(request):
    response = HttpResponse('设置cookies中')
    response.set_cookie('python1', 'information', max_age=20)
    response.set_cookie('python2', 'information of cookies', max_age=20)
    return response


# 访问另一个页面，打印cookies
def printcookies(request):
    cookies1 = request.COOKIES.get('python1')  # cookies对应的键值对
    cookies2 = request.COOKIES.get('python2')
    print(cookies1, cookies2, type(cookies1), type(cookies2))
    return render(request, 'web_1st/home.html', {'cookies1': cookies1, 'cookies2': cookies2})


def index(request):  # http://127.0.0.1:8000/webapp/
    return HttpResponse("问候：Hello,everyone!!!!Are you ok??")


def say(request):  # http://127.0.0.1:8000/webapp/say/
    index = reverse("webapp:index")
    # index视图函数的路由路径反查
    # index指的是web_1st中的urls.py的name，
    # webapp指的是Jango的urls.py的include()二元组的命名空间namespaces
    print(index)
    return HttpResponse(f"反查index={index}")


def weather(request, city, year):  # http://127.0.0.1:8000/webapp/weather/beijing/2019
    print(f"city={city}")
    print(f"year={year}")
    return HttpResponse(f"天气city={city},\tyear={year}")


def querystring(request):  # http://127.0.0.1:8000/webapp/querystring/?a=1&b=hehe&a=haha/
    # 处理请求路径里的查询字符串参数
    a = request.GET.get('a')
    b = request.GET.get('b')
    # b = request.POST.get('b')
    alist = request.GET.getlist('a')
    print(a + '\t' + b)
    return HttpResponse(f"query string--------a={a},b={b},a={alist}----------")


def formdata(request):  # http://127.0.0.1:8000/webapp/formdata/
    # 处理POST请求里的表单数据
    a = request.POST.get('a')
    a_list = request.POST.getlist('a')
    b = request.POST.get('b')
    c = request.POST.get('c')
    d = request.POST.get('d')
    print(f"a={a},a_list={a_list},b={b},c={c},d={d}")
    return HttpResponse(f"a={a},a_list={a_list},b={b},c={c},d={d}")


def jsondata(request):
    # 处理raw里面的json数据
    a = request.body
    a = json.loads(a)
    content_type = request.META['CONTENT_TYPE']
    print(type(a))
    return HttpResponse(f"{a},content_type={content_type}")


def loadfiles(request):
    # 文本信息content.txt
    with open(r"./JangoWeb/static/upload/content.txt", 'wb') as f:
        f.write(request.body)
    return HttpResponse(f"文件上传成功!!!!信息是:{request.body.decode()}")


def loadpictures(request):
    # 图片上传 picture.png
    with open(r"./JangoWeb/static/upload/picture.png", 'wb') as f:
        f.write(request.body)
    print(request.method, request.user, request.encoding, request.path)
    return HttpResponse(f"picture上传成功!!!!!")


def fileinform(request):
    with open(r"./JangoWeb/static/upload/daily.png", 'wb') as f:
        f.write(request.FILES.get('a'))
    return HttpResponse('文件上传成功!!!!')
