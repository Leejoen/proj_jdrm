from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autth.urls')),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('audits/', include('audits.urls')),
    path('events/', include('events.urls')),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
