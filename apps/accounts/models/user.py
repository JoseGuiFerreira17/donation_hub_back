from django.db.models import CharField, EmailField, DateTimeField, BooleanField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = CharField(verbose_name="nome completo", max_length=255)
    email = EmailField(verbose_name="endereço de e-mail", unique=True)
    phone = CharField(verbose_name="telefone", max_length=20, blank=True, null=True)
    role = CharField(
        max_length=50,
        choices=[
            ("admin", "Admin"),
            ("organization_admin", "Organization Admin"),
            ("viewer", "Viewer"),
        ],
    )
    is_staff = BooleanField(verbose_name="Pode acessar o painel", default=True)
    is_active = BooleanField(verbose_name="ativo", default=True)
    created_at = DateTimeField(verbose_name="criado em", auto_now_add=True)
    modified_at = DateTimeField(verbose_name="modificado em", auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
