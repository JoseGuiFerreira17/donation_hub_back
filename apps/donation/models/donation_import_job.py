from apps.core.models import BaseModel
from django.db.models import CharField, TextChoices


class DonationImportJob(BaseModel):
    class Status(TextChoices):
        PENDING = "PENDING", "Pendente"
        PROCESSING = "PROCESSING", "Processando"
        DONE = "DONE", "Concluído"
        ERROR = "ERROR", "Erro"

    file_path = CharField(verbose_name="Caminho do arquivo", max_length=255)
    status = CharField(
        verbose_name="Status",
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return self.file_path

    class Meta:
        verbose_name = "Importação de Doações"
        verbose_name_plural = "Importações de Doações"
        ordering = ["-created_at"]
