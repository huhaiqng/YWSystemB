from django.contrib import admin
from app.models import *
# from guardian.admin import GuardedModelAdmin
# Register your models here.
# class SoftwareProject(GuardedModelAdmin):
#     list_display = ('name',)

# class HostAdmin(GuardedModelAdmin):
#     list_display = ('ip',)

# admin.site.register(Host,HostAdmin)
admin.site.register(Env)
admin.site.register(Software)
# admin.site.register(Project,SoftwareProject)
