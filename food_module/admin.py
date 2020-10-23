from django.contrib import admin

from .models import dish,ingredient,step,nutrition
# Register your models here.
admin.site.register(dish)
admin.site.register(ingredient)
admin.site.register(step)
admin.site.register(nutrition)
