# Generated by Django 2.0.5 on 2018-07-05 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasking', '0001_initial_squashed_0005_auto_20180626_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskoccurrence',
            options={'ordering': ['task', 'location', 'date', 'start_time']},
        ),
        migrations.AddField(
            model_name='taskoccurrence',
            name='location',
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='tasking.Location',
                verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='task',
            name='locations',
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text='This represents the locations.',
                through='tasking.TaskLocation',
                to='tasking.Location',
                verbose_name='Locations'),
        ),
        migrations.AlterField(
            model_name='taskoccurrence',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='tasking.Task',
                verbose_name='Task'),
        ),
    ]