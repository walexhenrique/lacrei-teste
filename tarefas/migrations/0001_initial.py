# Generated by Django 4.1.2 on 2022-10-16 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarefa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("descricao", models.CharField(max_length=150)),
                ("data_e_hora_de_criacao", models.DateTimeField(auto_now_add=True)),
                ("ultima_modificacao", models.DateTimeField(auto_now=True)),
                ("finalizado", models.BooleanField(default=False)),
            ],
        ),
    ]
