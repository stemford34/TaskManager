# Generated by Django 2.0.7 on 2018-08-09 14:33

import TaskManager.myForm
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='day',
            new_name='repeat',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=TaskManager.myForm.TaskTypeField(choices=[('1', 'Task'), ('2', 'Goal')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
