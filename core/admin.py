from django.contrib import admin
from .models import BlogPost, Sermon, Testimony, Event, Appointment, PrayerRequest, NewsletterSubscriber


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date')
    fields = ('title', 'slug', 'content', 'date', 'image_url')  # ✅ URL-based image


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'date')


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name', 'content')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_date')
    fields = (
        'title',
        'location',
        'start_date',
        'end_date',
        'description',
        'image_url'  # ✅ switched from ImageField to URLField
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'preferred_date')


@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')