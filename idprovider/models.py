from django.db import models

ACCURACY = (
    ("year", "year"),
    ("month", "month"),
    ("day", "day"),
)


class IdProvider(models.Model):
    legacy_id = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data_status = models.CharField(
        max_length=300,
        blank=True,
        choices=(
            ("legacy-data", "legacy-data"),
            ("work-in-progress", "work-in-progress"),
            ("checked", "checked"),
        ),
        default="legacy-data",
    )

    class Meta:
        ordering = ["legacy_id"]

    def as_node(self):
        node = {}
        node["type"] = self.__class__.__name__
        node["label"] = self.__str__()
        node["id"] = f"{node['type'].lower()}__{self.id}"
        return node

    def status_color(self):
        if self.data_status == "legacy-data":
            return "danger"
        elif self.data_status == "work-in-progress":
            return "alert"
        else:
            return "success"
