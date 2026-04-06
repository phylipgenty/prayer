from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (
    BlogPost, Sermon, Testimony, Event, Appointment, 
    PrayerRequest, NewsletterSubscriber
)
from .forms import AppointmentForm

def index(request):
    latest_posts = BlogPost.objects.all().order_by('-date')[:3]
    latest_sermons = Sermon.objects.all().order_by('-date')[:3]
    return render(request, 'index.html', {
        'latest_posts': latest_posts,
        'latest_sermons': latest_sermons,
    })

def about(request):
    return render(request, 'about.html')

def events(request):
    events_list = Event.objects.all().order_by('start_date')
    return render(request, 'events.html', {'events': events_list})

def sermons(request):
    sermons_list = Sermon.objects.all()
    return render(request, 'sermons.html', {'sermons': sermons_list})

def testimonies(request):
    testimonies_list = Testimony.objects.all().order_by('-date')
    return render(request, 'testimonies.html', {'testimonies': testimonies_list})

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')

def donate(request):
    return render(request, 'donate.html')

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, 'Successfully subscribed to prayer notifications!')
            else:
                messages.info(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('index')

def prayer_request_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        PrayerRequest.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Prayer request sent. Our team will pray for you.')
    return redirect('index')

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username="prayer").exists():
        User.objects.create_superuser(
            username="prayer",
            password="PrayerPowerNetwork_2026"
        )
        return HttpResponse("Admin created")
    return HttpResponse("Admin already exists")