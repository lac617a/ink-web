from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from products.models import Products

# Create your models here.

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
  shipping_data   = models.TextField(verbose_name="Dato")
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