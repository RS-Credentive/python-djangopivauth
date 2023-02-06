from django.shortcuts import render
from django.views.generic import ListView

from .models import PivUser

# Create your views here.
class PivUserListView(ListView):
    """
    PivUserListView List currently configure PivUsers
    """

    model = PivUser
    context_object_name = "piv_users"
