from django.db import models

class GuestEmail(models.Model):
    email = models.EmailField()
    activate = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
