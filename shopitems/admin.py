from django.contrib import admin
from .models import ItemModel, ItemReveiw

# Register your models here.


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ("title", "user")


admin.site.register(ItemModel, ItemModelAdmin)


class ItemModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(ItemReveiw, ItemModelAdmin)
