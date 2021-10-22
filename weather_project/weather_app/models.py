from django.db import models
from django.db.models.fields import CharField, DateTimeField


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    icon_id = models.CharField(max_length=5)
    temperature = models.IntegerField()
    description  = models.TextField(max_length=20)
    created = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'cities'
        