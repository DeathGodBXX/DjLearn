from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
# WSGIRequest.accepted_types
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Customer, Order
from .forms import CustomerForm, OrderForm

# 响应cookies，如果为空设置cookies，否则跳过打印cookies
# request用于设置cookies，render用于渲染前端网页
# cookies是服务器端传送给客户端的，用于服务端辨认客户端
# def homepage(request):
#     # 视图函数决定渲染对象，对象模板继承自父模板
#     # 视图函数必须写子模版，渲染的是子模版，而不是父模板;
#     if request.COOKIES is None:
#         reponse = HttpResponse()
#         reponse.set_cookie('python1', 'infomation', max_age=30)
#         reponse.set_cookie('python2', 'infoandchang', max_age=30)
#         return reponse
#     return render(request, 'web_1st/home.html', {'cookies1': 'cookies1', "cookies2": "cookies2"})

# 设置cookies同时兼具访问
# def homepage(request):
#     if request.COOKIES is None:
#         response = HttpResponse('设置cookies中')
#         response.set_cookie('python1', 'information', max_age=20)
#         response.set_cookie('python2', 'information of cookies', max_age=20)
#         return response
#     try:
#         cookies1 = request.COOKIES.get('python1')
#         cookies2 = request.COOKIES.get('python2')
#         print(cookies1, cookies2, type(cookies1), type(cookies2))
#         return render(request, 'web_1st/home.html', {'cookies1': cookies1, 'cookies2': cookies2})
#     except:
#         return HttpResponse('网页错误')
#
#     response = render_to_string()
#     response.cookies('python')

# 渲染网页的同时设置cookies
# cookies用于状态保持，即使只登录一次，浏览器也会一致发送请求，cookies在底层已经封装了
# 估计不需要判断cookies存在与否，浏览器都自动带上，而且服务端只会发送一次。
# 设置cookies用HttpResponse对象，而render正好返回HttpResponse


# def homepage(request):
#     response = render(request, 'web_1st/home.html', {'cookies1': 'python1', 'cookies2': 'python2'})
#     # for i in range(1, 6):
#     #     response.set_cookie(f'python{i}', f'information__{randint(0,10)}', max_age=30)
#     return response

# @csrf_exempt
def homepage(request):
    if request.is_ajax:
        if request.POST.get('i-del'):
            del_order_id = request.POST.get('i-del')
            order = Order.objects.get(id=del_order_id)
            order.delete()
            return redirect("webapp:homepage")
        if request.POST.get('j-customer-del'):
            del_customer_id = request.POST.get('j-customer-del')
            customer = Customer.objects.get(id=del_customer_id)
            customer.delete()
            return redirect("webapp:homepage")

    customer = Customer.objects.all()  # objects是models.Manager为每一个新增class自动添加的，而objects是对应对象，内部定义了all()
    c_count = customer.count()

    order = Order.objects.all()  # objects成灰色的，应该是与我python虚拟环境和工作目录不在同级目录导致的
    total_count = order.count()

    pending_count = Order.objects.filter(status="Pending").count()  # 键值对，必须对应于类的指定属性
    out_for_delivery_count = Order.objects.filter(status="Out for delivery").count()
    delivered_count = Order.objects.filter(status="Delivered").count()

    last_five_order = []
    tag = 0
    for i in reversed(order):
        if tag < 5:
            last_five_order.append(i)
            tag += 1
        else:
            break


    context = {
        'customer': customer,
        'c_count': c_count,

        'total_count': total_count,
        'pending_count': pending_count,
        'out_for_delivery_count': out_for_delivery_count,
        'delivered_count': delivered_count,
        'order': last_five_order,
    }

    return render(request, "web_1st/home.html", context)


def create(request):
    if request.method == 'POST':
        if 'c-button' in request.POST:
            customer = CustomerForm(request.POST)
            if customer.is_valid():
                name = customer.cleaned_data['name']
                phone = customer.cleaned_data['phone']
                email = customer.cleaned_data['email']
                customer_create = Customer.objects.create(name=name, phone=phone, email=email)
                customer_create.save()
                return redirect('webapp:homepage')

        if 'o-button' in request.POST:
            order = OrderForm(request.POST)
            print(order)
            if order.is_valid():
                customer = order.cleaned_data['customer']
                product = order.cleaned_data['product']
                status = order.cleaned_data['status']
                order_create = Order.objects.create(customer=customer, product=product, status=status)
                order_create.save()
                return redirect('webapp:homepage')

    c_form = CustomerForm()
    o_form = OrderForm()

    context = {
        'c_form': c_form,
        'o_form': o_form,
    }
    return render(request, 'web_1st/create.html', context)


def view_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    c_form = CustomerForm(instance=customer)
    print(c_form)
    context = {
        'customer': customer,
        'c_form': c_form,
    }
    return render(request, 'web_1st/viewcustomer.html', context)


def update_order(request, pk):
    if request.method == 'POST':
        if 's-button' in request.POST:
            o_form = OrderForm(request.POST)
            if o_form.is_valid():
                customer = o_form.cleaned_data['customer']
                product = o_form.cleaned_data['product']
                status = o_form.cleaned_data['status']
                Order.objects.filter(id=pk).update(id=pk, customer=customer, product=product, status=status)
        return redirect('webapp:homepage')

    order = Order.objects.get(id=pk)
    o_form = OrderForm(instance=order)
    context = {
        'order': order,
        'o_form': o_form,
    }
    return render(request, 'web_1st/updateorder.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('webapp:homepage')

    context = {
        'order': order,
    }
    return render(request, 'web_1st/deleteorder.html', context)

