from django.contrib import admin
from . import models

admin.site.register(models.Report)
admin.site.register(models.Submissions)
admin.site.register(models.Announcements)
admin.site.register(models.NeighborlyHelp)
admin.site.register(models.Comments)

# Register your models here.
