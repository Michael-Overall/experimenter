# Generated by Django 2.1.11 on 2019-08-29 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("experiments", "0068_experiment_related_to")]

    operations = [
        migrations.AlterModelOptions(
            name="experimentemail",
            options={
                "ordering": ("sent_on",),
                "verbose_name": "Experiment Email",
                "verbose_name_plural": "Experiment Emails",
            },
        )
    ]
