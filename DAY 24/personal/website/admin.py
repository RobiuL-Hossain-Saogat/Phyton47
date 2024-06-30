from django.contrib import admin
from . models import Detail

# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    list_display=('name','mobile_number','address','email','image_url')

admin.site.register(Detail,DetailAdmin)