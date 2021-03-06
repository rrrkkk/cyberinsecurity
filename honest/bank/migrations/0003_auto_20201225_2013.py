# Generated by Django 3.1.4 on 2020-12-25 20:13

from django.db import migrations

def init_account2(apps,schema_editor):
    Account = apps.get_model('bank', 'Account')
    a = Account(id=1,username='bob',password='squarepants',balance=1)
    a.save()
    a = Account(id=2,username='angel',password='wings',balance=1000)
    a.save()
    a = Account(id=3,username='demon',password='horns',balance=-1000)
    a.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20201225_2001'),
    ]

    operations = [
        migrations.RunPython(init_account2),
    ]
