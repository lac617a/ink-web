from django import forms
from .models import Brands, Category, Products

class ProductsForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super(ProductsForm,self).__init__(*args,**kwargs)
    self.fields['pdImage'].widget.attrs = {
      'class':'form-control',
    }
  class Meta:
    model = Products
    fields = [
      'pdCode','pdName','pdPrice',
      'pdBrand','pdCategories',
      'pdDescription',
      'pdImage','pdState'
    ]
    widgets = {
      'pdCode':forms.NumberInput(attrs={'class':'form-control'}),
      'pdName':forms.TextInput(attrs={'class':'form-control'}),
      'pdPrice':forms.NumberInput(attrs={'class':'form-control'}),
      'pdBrand':forms.Select(attrs={'class':'form-select'}),
      'pdCategories':forms.Select(attrs={'class':'form-select'}),
      'pdDescription':forms.Textarea(attrs={'class':'form-control w-100'}),
      # 'pdImage':forms.TextInput(attrs={'class':'form-control','type':'file'}),
      'pdState':forms.CheckboxInput(attrs={'class':'form-check-input'})
    }

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['cgName']
    widgets = {
      'cgName':forms.TextInput(attrs={'class':'form-control'})
    }

class BrandForm(forms.ModelForm):
  class Meta:
    model = Brands
    fields = ['brName']
    widgets = {
      'brName':forms.TextInput(attrs={'class':'form-control'})
    }