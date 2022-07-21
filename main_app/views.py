from django.shortcuts import render
from .models import Mood

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def moods_index(request):
    moods = Mood.objects.all()
    return render(request, 'moods/index.html', {"moods": moods})

def moods_detail(request, mood_id):
  mood = Mood.objects.get(id=mood_id)
  return render(request, 'moods/detail.html', { 'mood': mood })