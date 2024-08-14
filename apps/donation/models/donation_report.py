from apps.core.models import BaseModel
from django.db.models import CharField, TextChoices


class DonationReport(BaseModel):
    class extnsions(TextChoices):
        PDF = "pdf", "pdf"
        CSV = "csv", "csv"
        XLSX = "xlsx", "xlsx"

    title = CharField(verbose_name="Título", max_length=255)
    format = CharField(verbose_name="Formato", max_length=10, choices=extnsions.choices)
    file_path = CharField(verbose_name="Caminho do arquivo", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Relatório de Doações"
        verbose_name_plural = "Relatórios de Doações"
        ordering = ["-created_at"]
