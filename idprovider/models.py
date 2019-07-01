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
    data_status = models.CharField(
        max_length=300, blank=True,
        choices=(
            ('legacy-data', 'legacy-data'),
            ('work-in-progress', 'work-in-progress'),
            ('checked', 'checked'),
        ),
        default="legacy-data"
    )

    def status_color(self):
        if self.data_status == "legacy-data":
            return 'danger'
        elif self.data_status == "work-in-progress":
            return 'alert'
        else:
            return 'success'
