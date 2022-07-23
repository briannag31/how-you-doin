from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('moods/', views.moods_index, name='index'),
    path('moods/<int:mood_id>/', views.moods_detail, name='detail'),
    path('moods/create/', views.MoodCreate.as_view(), name='moods_create'),
    path('moods/<int:pk>/update/', views.MoodUpdate.as_view(), name='moods_update'),
  path('moods/<int:pk>/delete/', views.MoodDelete.as_view(), name='moods_delete'),
  path('feelings/', views.FeelingList.as_view(), name='feelings_index'),
  path('feelings/<int:pk>/', views.FeelingDetail.as_view(), name='feelings_detail'),
  path('feelings/create/', views.FeelingCreate.as_view(), name='feelings_create'),
  path('feelings/<int:pk>/update/', views.FeelingUpdate.as_view(), name='feelings_update'),
  path('feelings/<int:pk>/delete/', views.FeelingDelete.as_view(), name='feelings_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('moods/<int:mood_id>/assoc_feeling/<int:feeling_id>/', views.assoc_feeling, name='assoc_feeling'),
]
