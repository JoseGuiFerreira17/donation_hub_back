from apps.core.models import BaseModel
from django.db.models import CharField, EmailField, ForeignKey, CASCADE


class Donor(BaseModel):
    name = CharField(verbose_name="Nome", max_length=255)
    email = EmailField(verbose_name="E-mail", unique=True)
    address = ForeignKey(
        "core.Address",
        verbose_name="Endereço",
        on_delete=CASCADE,
        related_name="donors",
    )
    phone = CharField(verbose_name="Telefone", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"
        ordering = ["-created_at"]
