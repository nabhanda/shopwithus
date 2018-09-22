from django.db import models
from django.db.models import CASCADE

from billing.models import BillingProfile

ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=CASCADE)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default="India")
    postal_code = models.CharField(max_length=6)

    def __str__(self):
        return str(self.billing_profile)
