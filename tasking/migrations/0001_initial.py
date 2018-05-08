# Generated by Django 2.0.5 on 2018-05-08 07:52

from django.db import migrations, models
import django.db.models.deletion
import tasking.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='Created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name',
                 models.CharField(
                     help_text='This represents the name.',
                     max_length=255,
                     verbose_name='Name')),
                ('description',
                 models.TextField(
                     blank=True,
                     default='',
                     help_text='This represents the description.',
                     verbose_name='Description')),
                ('target_object_id',
                 models.PositiveIntegerField(
                     blank=True, db_index=True, default=None, null=True)),
                ('start',
                 models.DateTimeField(
                     help_text='This is the date and time the task starts.',
                     verbose_name='Start')),
                ('end',
                 models.DateTimeField(
                     blank=True,
                     default=None,
                     help_text='This is the date and time the task starts.',
                     null=True,
                     verbose_name='Start')),
                ('timing_rule',
                 models.TextField(
                     help_text='This stores the rrule for recurrence.',
                     validators=[tasking.utils.validate_rrule],
                     verbose_name='Timing Rule')),
                ('total_submission_target',
                 models.IntegerField(
                     blank=True,
                     default=None,
                     help_text='This is the total number of submissions '
                               'required for this task. Set to None if '
                               'there is no Max.',
                     null=True,
                     verbose_name='Total Submissions Target')),
                ('user_submission_target',
                 models.IntegerField(
                     blank=True,
                     default=None,
                     help_text='This is the total number of submissions per '
                               'user required for this task. Set to None if '
                               'there is no Max.',
                     null=True,
                     verbose_name='User Submissions Target')),
                ('status',
                 models.CharField(
                     choices=[('a', 'Active'), ('b', 'Draft'), ('c',
                                                                'Closed')],
                     default='b',
                     help_text='The status of the Task',
                     max_length=1,
                     verbose_name='Status')),
                ('parent',
                 models.ForeignKey(
                     blank=True,
                     default=None,
                     help_text='This represents the parent task.',
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     to='tasking.Task',
                     verbose_name='Parent task')),
                ('target_content_type',
                 models.ForeignKey(
                     blank=True,
                     default=None,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='target',
                     to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'ordering': ['start', 'name', 'id'],
            },
        ),
    ]
