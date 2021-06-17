from django.contrib.auth.forms import AuthenticationForm

class FormLogin(AuthenticationForm):
  def __init__(self,*args,**kwargs):
    super(FormLogin,self).__init__(*args,**kwargs)
    self.fields['username'].widget.attrs = {
      'class':'form-control',
      'placeholder':'Ingrese de un nombre se usuario valido'
    }
    self.fields['password'].widget.attrs = {
      'class':'form-control',
      'placeholder':'Ingrese su contraseña'
    }