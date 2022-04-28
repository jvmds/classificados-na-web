# Generated by Django 4.0.4 on 2022-04-24 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classificados_na_web', '0003_categoria_tipoanuncio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='categoria',
            field=models.ManyToManyField(to='classificados_na_web.categoria'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='tipo_anuncio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classificados_na_web.tipoanuncio'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='descricao',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='observacao',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='telefone2',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
