from apps.core.models import BaseModel
from django.db.models import CharField, EmailField, DateField, ForeignKey, CASCADE


class Organization(BaseModel):
    name = CharField(verbose_name="Nome", max_length=255)
    cnpj = CharField(verbose_name="CNPJ", max_length=14)
    email = EmailField(verbose_name="E-mail", max_length=255)
    phone = CharField(verbose_name="Telefone", max_length=20)
    address = ForeignKey(
        "core.Address",
        verbose_name="Endereço",
        on_delete=CASCADE,
        related_name="organizations",
    )
    foundation_date = DateField(verbose_name="Data de Fundação", null=True, blank=True)
    website = CharField(verbose_name="Website", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organização"
        verbose_name_plural = "Organizações"
