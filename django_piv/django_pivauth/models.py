from django.db import models
from django.conf import settings
from typing import List


class PivUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject_dn = models.CharField(max_length=1000)  # TODO: What is the actual maximum length for a PIV DN?

    @property
    def allowed_issuers(self) -> List[str]:
        return settings.PIV_ALLOWED_ISSUERS

    @property
    def agency(self) -> str:
        # TODO: parse the subject DN and return the agency identifier
        return "Placeholder"
