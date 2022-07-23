from django.shortcuts import render, redirect
from .models import Mood, Feeling
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import NewEntryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def moods_index(request):
    moods = Mood.objects.filter(user=request.user)
    return render(request, 'moods/index.html', {"moods": moods})

@login_required
def moods_detail(request, mood_id):
  mood = Mood.objects.get(id=mood_id)
  return render(request, 'moods/detail.html', { 'mood': mood })

@login_required
def assoc_feeling(request, mood_id, feeling_id):
  Mood.objects.get(id=mood_id).feelings.add(feeling_id)
  return redirect('detail', mood_id=mood_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign-up - please try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class MoodCreate(LoginRequiredMixin, CreateView):
  model = Mood
  fields = ['date', 'headline', 'description', "designation"]
  success_url = '/moods/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MoodUpdate(LoginRequiredMixin, UpdateView):
  model = Mood
  fields = ['date', 'headline', 'description', "designation"]

class MoodDelete(LoginRequiredMixin, DeleteView):
  model = Mood
  success_url = '/moods/'

class FeelingList(LoginRequiredMixin, ListView):
  model = Feeling

class FeelingDetail(LoginRequiredMixin, DetailView):
  model = Feeling

class FeelingCreate(LoginRequiredMixin, CreateView):
  model = Feeling
  fields = '__all__'

class FeelingUpdate(LoginRequiredMixin, UpdateView):
  model = Feeling
  fields = ['name', 'designation']

class FeelingDelete(LoginRequiredMixin, DeleteView):
  model = Feeling
  success_url = '/feelings/'













# def new_mood(request, mood_id):
#   form = NewEntryForm(request.POST)
#   if form.is_valid():
#     new_mood = form.save(commit=False)
#     new_mood.mood_id = mood_id
#     new_mood.save()
#   return redirect('detail', {"mood_id":mood_id})