from django.db import models
from django.template.defaultfilters import truncatechars


class ContactRequest(models.Model):
    name = models.CharField(max_length=64, null=False)
    email_id = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=32, null=False)
    message = models.TextField(max_length=3000, null=False)

    def __str__(self):
        return f"From: {self.name} | Message: {truncatechars(self.message, 16)}"
