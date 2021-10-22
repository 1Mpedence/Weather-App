from django.contrib import admin
from .models import City

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'created')

admin.site.register(City, RatingAdmin)