from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,DetailView
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Brands, Category, Products
from .forms import ProductsForm

# Create your views here.

class ListProdView(View):
  model = Products
  paginate_by = 10
  template_name = 'products/list-products.html'
  
  def get_context_data(self,*args,**kwargs):
    context = {}
    context['paginate_by'] = args[0]
    context['qs'] = args[1]
    return context

  def get(self,request,*args,**kwargs):
    # SEEKER
    seeker = request.GET.get('search')
    get_state = self.model.objects.filter(pdState=True)
    if seeker:
      get_state = self.model.objects.filter(
        Q(pdName__icontains=seeker) |
        Q(pdDescription__icontains=seeker) 
      ).distinct()

    # PAGINATION
    count = 9
    paginate_by = request.GET.get('paginate_by',count) or count
    paginator = Paginator(get_state,paginate_by)
    page = request.GET.get('page')
    try:
      paginated = paginator.get_page(page)
    except PageNotAnInteger:
      paginated = paginator.get_page(1)
    except EmptyPage:
      paginated = paginator.page(paginator.num_pages)
    return render(request,self.template_name,self.get_context_data(paginate_by,paginated))

  def post(self,request,*args,**kwargs):
    pass

class MoreViewDetailProd(DetailView):
  model = Products
  template_name = 'products/more_view.html'

class GetCategoryProduView(View):
  model = Products
  template_name = 'products/get_select_prod_view.html'

  def get_context_data(self,*args,**kwargs):
    context = {}
    context['paginate_by'] = args[0]
    context['qs'] = args[1]
    return context

  def get(self,request,slug,*args,**kwargs):
    # SEEKER
    seeker = request.GET.get('search')
    get_state = self.model.objects.filter(pdState=True,pdCategories=Category.objects.get(cgName=slug))
    if seeker:
      get_state = self.model.objects.filter(
        Q(pdName__icontains=seeker) |
        Q(pdDescription__icontains=seeker),
        pdState=True,pdCategories=Category.objects.get(cgName=slug)
      ).distinct()
    
    count = 9
    paginate_by = request.GET.get('paginate_by',count) or count
    paginator = Paginator(get_state,paginate_by)
    page = request.GET.get('page')
    try:
      paginated = paginator.get_page(page)
    except PageNotAnInteger:
      paginated = paginator.get_page(1)
    except EmptyPage:
      paginated = paginator.page(paginator.num_pages)
    return render(request,self.template_name,self.get_context_data(paginate_by,paginated))

class GetBrandsProduView(GetCategoryProduView):

  def get(self,request,slug,*args,**kwargs):
    seeker = request.GET.get('search')
    get_state = self.model.objects.filter(pdState=True,pdBrand=Brands.objects.get(brName=slug))
    if seeker:
      get_state = self.model.objects.filter(
        Q(pdName__icontains=seeker) |
        Q(pdDescription__icontains=seeker),
        pdState=True,pdBrand=Brands.objects.get(brName=slug)
      ).distinct()
    
    count = 9
    paginate_by = request.GET.get('paginate_by',count) or count
    paginator = Paginator(get_state,paginate_by)
    page = request.GET.get('page')
    try:
      paginated = paginator.get_page(page)
    except PageNotAnInteger:
      paginated = paginator.get_page(1)
    except EmptyPage:
      paginated = paginator.page(paginator.num_pages)
    return render(request,self.template_name,self.get_context_data(paginate_by,paginated))















def productsHidden(request):
  get_hide = Products.objects.filter(pdState=False)
  print(get_hide)
  return render(request,'products/hide-products.html',{'query':get_hide})

def productDelete(request,id):
  get_item = get_object_or_404(Products,pk=id)
  if request.method == 'POST':
    get_item.delete()
    return redirect("Main:pro")
  return render(request,'products/delete-product.html',{'product':get_item})

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
      return redirect('Product:pro')
  except ObjectDoesNotExist as e:
    error =  e
  return render(request,
  'products/edit-product.html',
  {'query':pro_form,'error':error})
