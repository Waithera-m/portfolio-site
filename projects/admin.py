from django.contrib import admin
from projects.models import Repo

# Register your models here.
class RepoAdmin(admin.ModelAdmin):
    fields = ['project_name','description','url','project_image']

    list_display = ('project_name','pub_date')
    list_filter = ['pub_date']

admin.site.register(Repo,RepoAdmin)
