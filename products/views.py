from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Brands, Category, Products

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

class MoreViewDetailProd(View):
  model = Products
  template_name = 'products/more_view.html'

  def get_context_data(*args,**kwargs):
    context = {}
    context['object'] = args[1]
    context['error'] = args[2]
    return context

  def get(self,request,slug,*args,**kwargs):
    slug = slug.replace('-',' ')
    queryset = None
    error = None
    if slug:
      queryset = self.model.objects.filter(pdState=True).get(pdName__iexact=slug)
    else:
      error = 'A ocurrido un error, al parecer ese objeto a sido eliminado o no se encuentra disponible'
    return render(request,self.template_name,self.get_context_data(queryset,error))

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
    slug = slug.replace('-',' ')
    seeker = request.GET.get('search')
    get_state = self.model.objects.filter(pdState=True,pdCategories=Category.objects.get(cgName__iexact=slug))
    if seeker:
      get_state = self.model.objects.filter(
        Q(pdName__icontains=seeker) |
        Q(pdDescription__icontains=seeker),
        pdState=True,pdCategories=Category.objects.get(cgName=slug)
      ).distinct()
    
    count = 10
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
  model = Products
  template_name = 'products/get_select_prod_view.html'

  def get(self,request,slug,*args,**kwargs):
    slug = slug.replace('-',' ')
    seeker = request.GET.get('search')
    get_state = self.model.objects.filter(pdState=True,pdBrand=Brands.objects.get(brName__iexact=slug))
    if seeker:
      get_state = self.model.objects.filter(
        Q(pdName__icontains=seeker) |
        Q(pdDescription__icontains=seeker),
        pdState=True,pdBrand=Brands.objects.get(brName=slug)
      ).distinct()
    
    count = 10
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
