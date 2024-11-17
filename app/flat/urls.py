from django.urls import path

from . import views

app_name = "flat"
urlpatterns = [
    path("", views.FlatListView.as_view(), name="list"),
    path("create/", views.FlatCreateView.as_view(), name="create"),
    path("<uuid:pk>/", views.FlatDetailView.as_view(), name="detail"),
    # path("<int:pk>/update/", views.FlatUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", views.FlatDeleteView.as_view(), name="delete"),
]
