from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=50, help_text="YouTube video ID (e.g., dQw4w9WgXcQ)")
    preacher = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    preferred_date = models.CharField(max_length=50)
    preferred_time = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.preferred_date}"

class PrayerRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email