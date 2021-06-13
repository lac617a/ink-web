from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
  cgName    = models.CharField(max_length=100,verbose_name="Nombre de la categoria",null=True,blank=True)
  cgUpdate  = models.DateTimeField(auto_now_add=True)
  cgCreate  = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.cgName

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

@python_2_unicode_compatible
class Brands(models.Model):
  brName    = models.CharField(max_length=100,verbose_name="Nombre de la marca",help_text="Identifique la marca",unique=True)
  brUpdate  = models.DateTimeField(auto_now_add=True)
  brCreate  = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.brName

  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'

@python_2_unicode_compatible
class Products(models.Model):
  pdUser        = models.ForeignKey(to=User,on_delete=models.CASCADE)
  pdCode        = models.IntegerField(unique=True,verbose_name="Codigo del producto",help_text="Es requerido")
  pdName        = models.CharField(max_length=100,verbose_name="Nombre del pruducto")
  pdPrice       = models.DecimalField(decimal_places=3,max_digits=100000,verbose_name="Precio de venta",help_text="Tome en cuenta el precio adecuado para su producto")
  pdBrand       = models.ForeignKey(Brands,on_delete=models.CASCADE,verbose_name="Marca del producto",help_text="Este campo es requerido",blank=True)
  pdCategories  = models.ForeignKey(to=Category,on_delete=models.CASCADE, verbose_name="Categoria relacionada con el producto")
  pdDescription = RichTextField(verbose_name="Descripcion del producto")
  pdLikes       = models.ManyToManyField(User,related_name="likes",blank=True)
  pdStock       = models.IntegerField(default=0)
  pdImage       = models.ImageField(upload_to="products/%Y/%m/%d",verbose_name="Cargar una imagen para el producto",null=True,blank=True)
  pdState       = models.BooleanField(default=True, verbose_name="visto / oculto")
  pdUpdate      = models.DateTimeField(auto_now_add=True)
  pdCreate      = models.DateTimeField(auto_now_add=True)

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
  slUpdate        = models.DateTimeField(auto_now_add=True)
  slCreate        = models.DateTimeField(auto_now_add=True)

@python_2_unicode_compatible
class OrderItem(models.Model):
  oiUser    = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name="Usuario")
  oiItem    = models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name="Articulo")
  oiAmount  = models.IntegerField(default=1,verbose_name="Cantidad")
  ordered   = models.BooleanField(default=False,verbose_name="Ordenado / Ordenar")

  class Meta:
    ordering = ['-id']
    verbose_name = 'Articulo ordenado'
    verbose_name_plural = 'Articulos ordenados'

  def __str__(self):
    return f"{self.ioAmunt} de {self.item.pdPrice}"

  def get_total_price(self):
    return self.oiAmount * self.item.pdPrice



@python_2_unicode_compatible
class Order(models.Model):
  odUser          = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario")
  odItem          = models.ManyToManyField(OrderItem,verbose_name="Articulo")

  shipping_calle  = models.CharField(max_length=256,verbose_name="Calle")
  shipping_number = models.CharField(max_length=256,verbose_name="Numero")
  shipping_data   = TextField(verbose_name="Dato")
  shipping_phone  = models.CharField(max_length=10,verbose_name="Telefono")

  start_date      = models.DateTimeField(auto_now_add=True,blank=True)
  ordered_date    = models.DateTimeField(auto_now_add=True,blank=True)
  ordered         = models.BooleanField(default=False,verbose_name="Ordenado / Ordenar")

  class Meta:
    ordering = ['-id']
    verbose_name = 'Pedido' 
    verbose_name_plural = 'Pedidos' 

  def __str__(self):
    return self.user.usuario.username

  def get_total(self):
    total = 0
    for order_item in self.item.all():
      total += order_item.get_total_price()
    return total