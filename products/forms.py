from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super(ProductsForm,self).__init__(*args,**kwargs)
    self.fields['pdCode'].widget.attrs = {
      'class':'form-control',
      'required': True
    }
    self.fields['pdName'].widget.attrs = {
      'class':'form-control',
      'required': True
    }
    self.fields['pdPrice'].widget.attrs = {
      'class':'form-control',
    }
    self.fields['pdBrand'].widget.attrs = {
      'class':'form-select',
      'required': True
    }
    self.fields['pdCategories'].widget.attrs = {
      'class':'form-select',
      'required': True
    }
    self.fields['pdDescription'].widget.attrs = {
      'class':'form-control w-100',
      'rows':5,
    }
    self.fields['pdStock'].widget.attrs = {
      'class':'form-control',
    }
    self.fields['pdImage'].widget.attrs = {
      'class':'form-control',
    }
    self.fields['pdState'].widget.attrs = {
      'class':'form-check-input',
    }
  class Meta:
    model = Products
    fields = [
      'pdCode','pdName','pdPrice',
      'pdBrand','pdCategories',
      'pdDescription','pdStock',
      'pdImage','pdState'
    ]
    # widgets = {
    #   'pdBrand':forms.SelectMultiple(attrs={'class':'form-control'}),
    #   'pdCategories':forms.SelectMultiple(attrs={'class':'form-control'})
    # }