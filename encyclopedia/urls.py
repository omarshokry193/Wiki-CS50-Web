from django.urls import path

from . import views
app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("create-page",views.createEntry, name='create-entry'),
    path("wikipedia/<str:entry>",views.getEntry, name='entry-url'),
    path("wikipedia/<str:entry>/edit",views.editEntry, name='edit-entry'),
    path("random-page",views.randomEntry, name='random-entry'),
    path("search", views.searchEntry, name='search-entry')
]
