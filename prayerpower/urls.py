from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth.models import User

# 👇 temporary admin fix view
def create_admin(request):
    if not User.objects.filter(username="prayer").exists():
        User.objects.create_superuser(
            username="prayer",
            password="PrayerPowerNetwork_2026"
        )
        return HttpResponse("Admin created successfully")
    return HttpResponse("Admin already exists")

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 ADD THIS LINE
    path('fix-admin/', create_admin),

    path('', include('core.urls')),
]