# Generated by Django 4.2.6 on 2023-12-23 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xeroxapp', '0015_studentpdflist_studentpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ownerorders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slno', models.IntegerField()),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('ownerPDFlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xeroxapp.ownerpdflist')),
            ],
        ),
    ]