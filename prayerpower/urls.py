from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# import the reset view (TEMPORARY)
from core.views import reset_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    # TEMP FIX: remove after use
    path('reset-admin/', reset_admin),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)