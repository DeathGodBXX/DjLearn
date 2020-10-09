from django.urls import path, re_path

from . import views, viewstest

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),


    path('viewcustomer/<str:pk>/', views.view_customer, name='viewcustomer'),
    path('updateorder/<str:pk>/', views.update_order, name='updateorder'),
    path('deleteorder/<str:pk>/', views.delete_order, name='deleteorder'),



    path('setcookies/', viewstest.setcookies, name='setcookies'),
    path('printcookies/', viewstest.printcookies, name='printcookies'),
    path('index/', viewstest.index, name='index'),
    # 第一个参数是子应用路由，name反解析index的子路由
    path('say/', viewstest.say, name='say'),
    re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>[0-9]+)/$', viewstest.weather, name='weather'),
    # re_path用于正则匹配
    # 正则匹配，第一层脱去webapp/,剩下weather/城市/年份
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    path('querystring/', viewstest.querystring, name='querystring'),
    path('formdata/', viewstest.formdata, name='formdata'),
    path('jsondata/', viewstest.jsondata, name='jsondata'),
    path('loadfiles/', viewstest.loadfiles, name='loadfiles'),
    path('loadpictures/', viewstest.loadpictures, name='loadpictures'),
    path('fileinform/', viewstest.fileinform, name='fileinform'),
]
