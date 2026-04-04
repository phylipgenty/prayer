from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('sermons/', views.sermons, name='sermons'),
    path('testimonies/', views.testimonies, name='testimonies'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),
    path('donate/', views.donate, name='donate'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
    path('prayer-request/', views.prayer_request_submit, name='prayer_request'),
]