from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login,logout
from .forms import FormLogin

# Create your views here.
"""
Aqui lo que intentamos hacer es un login de una manera mas
segura y eficaz asi que analizalo con cuidado.
"""

class Login(FormView):
  template_name = ''
  form_class = FormLogin
  success_url = reverse_lazy('Product:list-products')

  @method_decorator(csrf_protect)
  @method_decorator(never_cache)
  def dispatch(self,request,*args,**kwargs):
    if request.user.is_authenticated:
      return HttpResponseRedirect(self.get_success_url())
    else:
      return super(Login,self).dispatch(request,*args,**kwargs)

  def form_valid(self,form):
    login(self.request,form.get_user())
    return super(Login,self).form_valid(form)

def logoutUser(request):
  logout(request)
  return HttpResponseRedirect('/accounts/login/')