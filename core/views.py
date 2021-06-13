from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Products
from .forms import ProductsForm
# Create your views here.

def windowMain(request):
  if request.method == 'POST':
    subject = request.POST.get('subject')
    mail = request.POST.get('mail')
    message = request.POST.get('content') + f' |Remitente {mail}'
    gmail = settings.EMAIL_HOST_USER
    email_from = gmail

    recipent_list = [gmail]
    send_mail(subject,message,email_from,recipent_list)
    return redirect('/')
  return render(request,'home.html')

def termsAndConditions(request):
  return render(request,'termsAndCondition.html')

def productsViews(request):
  qs = Products.objects.filter(pdState=True)
  return render(request,'products.html',{'qs':qs})

def productsHidden(request):
  get_hide = Products.objects.filter(pdState=False)
  print(get_hide)
  return render(request,'components/products/hide-products.html',{'query':get_hide})

def productDelete(request,id):
  get_item = get_object_or_404(Products,pk=id)
  if request.method == 'POST':
    get_item.delete()
    return redirect("Main:pro")
  return render(request,'components/products/delete-product.html',{'product':get_item})

def productEdit(request,id):
  pro_form = None
  error = None
  try:
    get_product = Products.objects.get(pk=id)
    if request.method == 'GET':
      pro_form = ProductsForm(instance=get_product)
    else:
      pro_form = ProductsForm(request.POST,instance=get_product)
      if pro_form.is_valid():
        pro_form.save()
      return redirect('Main:pro')
  except ObjectDoesNotExist as e:
    error =  e
  return render(request,
  'components/products/edit-product.html',
  {'query':pro_form,'error':error})
