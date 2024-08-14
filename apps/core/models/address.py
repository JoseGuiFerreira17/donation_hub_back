from apps.core.models import BaseModel
from django.db.models import CharField
from apps.core.choices.choices import STATE_CHOICES


class Address(BaseModel):
    street = CharField(verbose_name="Rua", max_length=255)
    number = CharField(verbose_name="Número", max_length=10, blank=True, null=True)
    complement = CharField(
        verbose_name="Complemento", max_length=255, blank=True, null=True
    )
    neighborhood = CharField(verbose_name="Bairro", max_length=255)
    city = CharField(verbose_name="Cidade", max_length=255)
    state = CharField(verbose_name="Estado", max_length=2, choices=STATE_CHOICES)
    zip_code = CharField(verbose_name="CEP", max_length=9)

    def __str__(self):
        return f"{self.street}, {self.number}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
