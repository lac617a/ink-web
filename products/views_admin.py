from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.views.generic import View,ListView
from django.db.models import Q
from .models import Category, Products,Brands
from .forms import CategoryForm, ProductsForm,BrandForm

class ListProdViewAdmin(View):
  model = Products
  paginate_by = 10
  template_name = 'adminProduct/products/lists-products.html'

  def get_queryset(self,seeker=None):
    queryset = self.model.objects.filter(pdState=True)
    if seeker is not None:
      queryset = self.model.objects.filter(
        Q(pdName__icontains=seeker) |
        Q(pdCode__contains=seeker),
        pdState=True
      ).distinct()
    return queryset

  def get_context_data(self,*args,**kwargs):
    context = {}
    context['paginate_by'] = args[0]
    context['qs'] = args[1]
    context['total_products'] = self.get_queryset().count()
    return context
  
  def get(self,request,*args,**kwargs):
    COUNT = 10
    searchCode = request.GET.get('searchCode')
    paginate_by = request.GET.get('paginate_by',COUNT) or COUNT
    paginator = Paginator(self.get_queryset(searchCode),paginate_by)
    page = request.GET.get('page')
    try:
      paginated = paginator.get_page(page)
    except PageNotAnInteger:
      paginated = paginator.get_page(1)
    except EmptyPage:
      paginated = paginator.page(paginator.num_pages)
    return render(request,self.template_name,self.get_context_data(paginate_by,paginated))


class AddProdViewAdmin(CreateView):
  model = Products
  template_name = 'adminProduct/products/products_create_form.html'
  form_class = ProductsForm

  def get_context_data(self,*args,**kwargs):
    context = super().get_context_data(*args,**kwargs)
    context['qs'] = self.model.objects.filter(pdState=True)
    return context

  def post(self,request,*args,**kwargs):
    form = self.form_class(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('Admin:listProducts')
    else:
      return redirect('Admin:listProducts')

class UpdateProdViewAdmin(UpdateView):
  model = Products
  form_class = ProductsForm
  template_name = 'adminProduct/products/edit-products.html'
  success_url = reverse_lazy('Admin:listProducts')

  def get_context_data(self,*args,**kwargs):
    context = super().get_context_data(*args,**kwargs)
    context['qs'] = self.model.objects.filter(pdState=True)
    return context

class DeleteProdViewAdmin(DeleteView):
  model = Products
  def post(self,request,pk,*args,**kwargs):
    object = self.model.objects.get(pk=pk)
    object.pdState = False
    object.save()
    return redirect('Admin:listProducts')


"""
CRUD CON LAS CATEGORIAS AND MARCAS
"""

class ListCategoryView(ListProdViewAdmin):
  model = Category
  form_class = CategoryForm
  template_name = 'adminProduct/category/list-category.html'

  def get_queryset(self,seeker=None):
    return self.model.objects.all()

class UpdateCategoryView(UpdateView):
  model = Category
  template_name = 'adminProduct/category/edit-category.html'
  form_class = CategoryForm
  success_url = reverse_lazy('Admin:listCategory')

class AddCategoryView(CreateView):
  modal = Category
  template_name = 'adminProduct/category/category_create_form.html'
  form_class = CategoryForm
  success_url = reverse_lazy('Admin:listCategory')

class DeleteCategoryView(DeleteView):
  model = Category
  template_name = 'adminProduct/category/category_confirm_delete.html'
  success_url = reverse_lazy('Admin:listCategory')


#!Marcas

class ListBrandView(ListProdViewAdmin):
  model = Brands
  form_class = BrandForm
  template_name = 'adminProduct/brands/list-brand.html'

  def get_queryset(self,seeker=None):
    return self.model.objects.all()
class UpdateBrandView(UpdateView):
  model = Brands
  template_name = 'adminProduct/brands/edit-brand.html'
  form_class = BrandForm
  success_url = reverse_lazy('Admin:listBrand')

class AddBrandView(CreateView):
  modal = Brands
  template_name = 'adminProduct/brands/brand_create_form.html'
  form_class = BrandForm
  success_url = reverse_lazy('Admin:listBrand')


class DeleteBrandView(DeleteView):
  model = Brands
  template_name = 'adminProduct/brands/brand_confirm_delete.html'
  success_url = reverse_lazy('Admin:listBrand')
