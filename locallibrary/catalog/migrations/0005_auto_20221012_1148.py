# Generated by Django 3.2.16 on 2022-10-12 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance_wbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.RenameField(
            model_name='bookinstance',
            old_name='wbook',
            new_name='book',
        ),
    ]
