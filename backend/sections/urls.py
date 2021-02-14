from django.urls import path
from .views import SectionCreateView, SectionsListView, SectionDetailView


app_name = 'sections'
urlpatterns = [
    path('section/create/', SectionCreateView.as_view()),
    path('all/', SectionsListView.as_view()),
    path('section/detail/<int:pk>', SectionDetailView.as_view()),
]
