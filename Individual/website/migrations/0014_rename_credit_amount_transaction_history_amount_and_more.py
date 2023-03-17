# Generated by Django 4.1.7 on 2023-03-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0013_register_login_role"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction_history",
            old_name="credit_amount",
            new_name="amount",
        ),
        migrations.RemoveField(
            model_name="transaction_history",
            name="debit_amount",
        ),
        migrations.AddField(
            model_name="transaction_history",
            name="type_amount",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
