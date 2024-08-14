from apps.core.models import BaseModel
from django.db.models import (
    DecimalField,
    ForeignKey,
    CASCADE,
    DateField,
    TextField,
)


class Donation(BaseModel):
    amount = DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)
    donor = ForeignKey(
        "donation.Donor",
        verbose_name="Doador",
        on_delete=CASCADE,
        related_name="donations",
    )
    date = DateField(verbose_name="Data")
    organization = ForeignKey(
        "organization.Organization",
        verbose_name="Organização",
        on_delete=CASCADE,
        related_name="donations",
    )
    notes = TextField(verbose_name="Observações", blank=True, null=True)

    def __str__(self):
        return f"{self.donor} - {self.amount}"

    class Meta:
        verbose_name = "Doação"
        verbose_name_plural = "Doações"
        ordering = ["-created_at"]
