from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class WebResource(resources.ModelResource):
    class Meta:
        model = Web

class AdminCategory(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'state', 'creationDate')
    search_fields = ['name']
    resource_class = CategoryResource

admin.site.register(Category,AdminCategory)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Web)
admin.site.register(SocialNetworks)
admin.site.register(Contact)
admin.site.register(Suscription)

# Register your models here.
