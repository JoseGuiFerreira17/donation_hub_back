from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from apps.accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "role",
            "is_staff",
            "is_active",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ("id", "created_at", "modified_at")


class UserUpdatePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True)
    password_confirmation = CharField(write_only=True)
    last_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["password", "password_confirmation", "last_password"]

    def validate(self, data):
        user = self.instance
        if not user.check_password(data["last_password"]):
            raise ValidationError("Senha antiga não confere")

        if data["password"] != data["password_confirmation"]:
            raise ValidationError("As senhas não conferem")
        return data
