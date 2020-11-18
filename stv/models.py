from django.db import models

# Create your models here.


class cliente(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(default='null',upload_to="clientes")
    web = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title}"
    


class conocimiento(models.Model):

    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"

class proyecto(models.Model):

    title = models.CharField(max_length=30)
    image = models.ImageField(default='null')
    web = models.CharField(max_length=100)
  
    def __str__(self):
        return f"{self.title}"