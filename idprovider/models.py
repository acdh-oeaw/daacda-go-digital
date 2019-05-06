from django.db import models

ACCURACY = (
    ('year', 'year'),
    ('month', 'month'),
    ('day', 'day'),
)


class IdProvider(models.Model):
    legacy_id = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
