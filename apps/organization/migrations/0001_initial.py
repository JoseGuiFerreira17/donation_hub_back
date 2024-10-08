# Generated by Django 4.2.15 on 2024-08-14 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('foundation_date', models.DateField(blank=True, null=True, verbose_name='Data de Fundação')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='core.address', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Organização',
                'verbose_name_plural': 'Organizações',
            },
        ),
    ]
