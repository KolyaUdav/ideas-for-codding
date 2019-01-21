from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ideas/', views.IdeaListView.as_view(), name='list'),
    path('ideas/<pk>/', views.IdeaDetailView.as_view()),
    path('random/', views.IdeaRandomView.as_view()),
]

