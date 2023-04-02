# Generated by Django 4.1.7 on 2023-04-02 02:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='id',
        ),
        migrations.AddField(
            model_name='movies',
            name='id_filme',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
