from django.db.models import Model, DateTimeField, BooleanField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_active = BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
