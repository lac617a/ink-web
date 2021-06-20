from django.db import models

class Computer(models.Model):
  name = models.CharField(verbose_name="Nombre de la Marca",max_length=20)
  image = models.ImageField(upload_to='logos/computer')
  created = models.DateField(auto_now=True,auto_now_add=False)
  update = models.DateField(auto_now=True,auto_now_add=False)

  def __str__(self):
    return self.name

class Printer(models.Model):
  name = models.CharField(verbose_name="Nombre de impresora",max_length=20)
  image = models.ImageField(upload_to='logos/computer')
  created = models.DateField(auto_now=True,auto_now_add=False)
  update = models.DateField(auto_now=True,auto_now_add=False)

  def __str__(self):
    return self.name