from django.contrib import admin
from test_app.models import FetchModel
# Register your models here.

class FetchModelAdmin(admin.ModelAdmin):
    list_display = ['url','title','description','price','mobile_number','size']

admin.site.register(FetchModel,FetchModelAdmin)
