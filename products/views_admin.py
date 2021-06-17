from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DeleteView,UpdateView
from .models import Products
from .views import ListProdView
from .forms import ProductsForm

class ListProdViewAdmin(ListProdView):
  template_name = 'adminProduct/products/lists-products.html'
  form_class = ProductsForm

  def get_queryset(self):
    return self.model.objects.filter(pdState=True)

  def get_context_data(self,*args,**kwargs):
    context = super().get_context_data(*args,**kwargs)
    context['form'] = self.form_class
    return context
  
  def get(self,request,*args,**kwargs):
    count = 10
    paginate_by = request.GET.get('paginate_by',count) or count
    paginator = Paginator(self.get_queryset(),paginate_by)
    page = request.GET.get('page')
    try:
      paginated = paginator.get_page(page)
    except PageNotAnInteger:
      paginated = paginator.get_page(1)
    except EmptyPage:
      paginated = paginator.page(paginator.num_pages)
    return render(request,self.template_name,self.get_context_data(paginate_by,paginated))

  # Crear productos
  # def post(self,request,*args,**kwargs):
  #   form = self.form_class(request.POST,request.FILES)
  #   if form.is_valid():
  #     form.save()
  #     return redirect('Admin:list-products')
  #   else:
  #     form = self.form_class()
  #     return render(request,self.template_name,self.get_context_data())


class UpdateProdViewAdmin(UpdateView):
  model = Products
  form_class = ProductsForm
  template_name = 'adminProduct/products/edit-products.html'
  success_url = reverse_lazy('Admin:list-products')

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
    return redirect('Admin:list-products')