# Generated by Django 3.1.4 on 2022-03-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userexcuse',
            name='excuse',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userexcuse',
            name='excuse_category',
            field=models.CharField(choices=[('family', 'Family'), ('office', 'Office'), ('children', 'Children'), ('college', 'College'), ('party', 'Party')], max_length=45),
        ),
    ]
