# Generated by Django 4.2.6 on 2023-12-20 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xeroxapp', '0007_alter_credentiallist_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credentiallist',
            options={'verbose_name_plural': 'CredentialList'},
        ),
        migrations.AlterModelOptions(
            name='credentials',
            options={'verbose_name_plural': 'Credentials'},
        ),
        migrations.AlterModelOptions(
            name='ownerpdflist',
            options={'verbose_name_plural': 'ownerPDFlist'},
        ),
    ]
