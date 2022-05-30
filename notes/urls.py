from django.urls import path
from notes import views
urlpatterns = [
    path('', views.mainPage , name='notesMainPage'),
    path('notes', views.index , name='notes'),
    path('search-results', views.searchResults , name='search-subject')
]


# traintoolz.com/nots/