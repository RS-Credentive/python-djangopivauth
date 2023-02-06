from django.urls import path

from . import views

urlpatterns = [
    path("piv_users/", views.PivUserListView.as_view(), name="piv_users_list"),
]
