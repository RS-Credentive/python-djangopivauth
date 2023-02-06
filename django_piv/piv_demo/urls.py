from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShowPivUserView.as_view()),
]
