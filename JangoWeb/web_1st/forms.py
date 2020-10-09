from django import forms
from django.forms import ModelForm

# Create your forms here
from .models import Customer, Product, Order


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['time_created']

        labels = {
            'name': '姓名',
            'phone': '电话',
            'email': '邮箱',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入姓名',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入电话',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱'
            })
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['time_created']

        labels = {
            'customer': '顾客',
            'product': '商品',
            'status': '状态',
        }

        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            })
        }
