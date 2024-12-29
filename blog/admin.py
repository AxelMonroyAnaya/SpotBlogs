from django.contrib import admin
from .models import Categoria, Articulo

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields =('created_at',)
    search_fields=('name','description')
    list_filter=('created_at',)
    list_display=('name','created_at',)
class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields =('user','created_at',)
    search_fields=('title','content',)
    list_filter=('created_at','public',)
    list_display=('title','public','created_at','user',)


    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id=request.user.id
        obj.save()


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
# Register your models here.
