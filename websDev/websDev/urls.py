from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),      
    path('bypass/', views.bypass, name='bypass'), 
    path('byreject/', views.byreject, name='byreject'), 
    path('detail-pass/', views.DetailPass, name='DetailPass'), 
    path('detail-reject/', views.DetailReject, name='DetailReject'), 
]

if settings.DEBUG:                                                                              
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
