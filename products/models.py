from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
  cgName    = models.CharField(max_length=100,verbose_name="Nombre de la categoria",null=True,blank=True)
  cgUpdate  = models.DateTimeField(auto_now_add=False,auto_now=True)
  cgCreate  = models.DateTimeField(auto_now_add=False,auto_now=True)

  def __str__(self):
    return self.cgName

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

@python_2_unicode_compatible
class Brands(models.Model):
  brName    = models.CharField(max_length=100,verbose_name="Nombre de la marca",help_text="Identifique la marca",unique=True)
  brUpdate  = models.DateTimeField(auto_now_add=False,auto_now=True)
  brCreate  = models.DateTimeField(auto_now_add=False,auto_now=True)

  def __str__(self):
    return self.brName

  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'

@python_2_unicode_compatible
class Products(models.Model):
  pdCode        = models.IntegerField(unique=True,verbose_name="Codigo del producto",help_text="Es requerido")
  pdName        = models.CharField(max_length=60,verbose_name="Nombre del pruducto",blank=False)
  pdPrice       = models.DecimalField(decimal_places=3,max_digits=100000,verbose_name="Precio de venta",help_text="Tome en cuenta el precio adecuado para su producto",blank=False)
  pdBrand       = models.ForeignKey(Brands,on_delete=models.CASCADE,verbose_name="Marca del producto",help_text="Este campo es requerido",blank=True)
  pdCategories  = models.ForeignKey(to=Category,on_delete=models.CASCADE, verbose_name="Categoria relacionada con el producto")
  pdDescription = RichTextField(verbose_name="Descripcion del producto")
  pdLikes       = models.ManyToManyField(User,related_name="likes",blank=True)
  pdStock       = models.IntegerField(default=0)
  pdImage       = models.ImageField(upload_to="products/%Y/%m/%d",verbose_name="Cargar una imagen para el producto",null=True,blank=True)
  pdState       = models.BooleanField(default=True, verbose_name="Estado = Visto/Oculto")
  pdUpdate      = models.DateTimeField(auto_now=True, auto_now_add=False)
  pdCreate      = models.DateTimeField(auto_now=True,auto_now_add=False)

  def total_likes(self):
    return self.likes.count()

  def con_likes(self):
    return self.likes.count() - 1

  def __str__(self):
    return self.pdName

  def get_image_url(self):
    if self.pdImage and hasattr(self.pdImage,'url'):
      return self.pdImage.url
    else:
      return '/static/img/loaderErrorImage.png'

  class Meta:
    ordering = ['-id']
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'

class Supplier(models.Model):
  TYPE_DOC        = [('Nit','Nit'),('Cédula','Cedula'),('Otro','Otro')]
  slBusiness      = models.CharField(max_length=50,verbose_name="Nombre de la empresa")
  slTypeDoc       = models.CharField(max_length=6,choices=TYPE_DOC,default=TYPE_DOC[0][0],verbose_name="Tipo de documento")
  slNumberDoc     = models.IntegerField(verbose_name="Numero del Dcumento", unique=True)
  slBusinessPhone = models.IntegerField(verbose_name="Numero telefonico de la empresa")
  slBusinessUrl   = models.URLField(verbose_name="Sitio web de la empresa",unique=True, blank=True, help_text="No es requerido")
  slUpdate        = models.DateTimeField(auto_now_add=False,auto_now=True)
  slCreate        = models.DateTimeField(auto_now_add=False,auto_now=True)