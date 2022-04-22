from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', '_autor'] # O _autor chama a função _autor
    exclude = ['autor',]

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        queryset = queryset.filter(autor=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)