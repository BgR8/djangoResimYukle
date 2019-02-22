from django.db import models

# Create your models here.
class Resim(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title