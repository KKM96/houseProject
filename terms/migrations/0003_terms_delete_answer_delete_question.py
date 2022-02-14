# Generated by Django 4.0.2 on 2022-02-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0002_alter_answer_id_alter_question_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Term_name', models.CharField(max_length=1000)),
                ('Term_def', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'terms',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
