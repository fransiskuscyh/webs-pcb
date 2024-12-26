from django.contrib import admin
from .models import Bypassmode

admin.site.register(Bypassmode)

admin.site.site_header = "Control Panel"
admin.site.site_title = "Panel Admin"
admin.site.index_title = "Welcome"
