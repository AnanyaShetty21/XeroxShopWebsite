# Generated by Django 4.2.6 on 2023-12-20 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xeroxapp', '0004_alter_ownerpdflist_options_alter_pdf_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ownerpdflist',
            options={'verbose_name': 'ownerPDFlist', 'verbose_name_plural': 'ownerPDFlists'},
        ),
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('CredentialList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xeroxapp.credentiallist')),
            ],
        ),
    ]