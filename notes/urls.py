from django.urls import path
from notes import views
urlpatterns = [
    path('', views.index , name='notesIndex'),
    path('search-results', views.searchResults , name='search-subject')
]