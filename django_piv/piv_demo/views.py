from django.shortcuts import render
from django.views.generic import TemplateView

from typing import Any, Dict

# Create your views here.
class ShowPivUserView(TemplateView):
    """
    ShowPivUserView Shows information about the PIV User based on server headers
    """

    template_name = "show_piv_user.dtl"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["meta"] = self.request.META
        context["headers"] = self.request.headers
        return context
