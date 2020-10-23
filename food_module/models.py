from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class dish(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    minutes = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=50000,null=True,blank=True)
    img = models.ImageField(upload_to="dishes",default="default.jpg",null=True,blank=True)

    class Meta:
        verbose_name_plural="dishes"

    def __str__(self):
        return self.name
class ingredient(models.Model):
    name=models.CharField(max_length=1000,null=True,blank=True)
    dish=models.ForeignKey(dish,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class step(models.Model):
    number=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=10000,null=True,blank=True)
    dish=models.ForeignKey(dish,on_delete=models.CASCADE)

class nutrition(models.Model):
    calories = models.FloatField(_('calories'),null=True,blank=True)
    total_fat = models.FloatField(_('total fat'),null=True,blank=True)
    sugar = models.FloatField(null=True,blank=True)
    sodium = models.FloatField(null=True,blank=True)
    protein = models.FloatField(null=True,blank=True)
    saturated_fat = models.FloatField(_('saturated fat'),null=True,blank=True)
    carbohydrates = models.FloatField(null=True,blank=True)
    dish=models.ForeignKey(dish,on_delete=models.CASCADE,null=True,blank=True)
