# Generated by Django 4.0.5 on 2022-06-25 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_courses_course_instructor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_credits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tests',
            name='test_subject',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_name', models.CharField(max_length=100)),
                ('curriculum_duration', models.IntegerField()),
                ('Total_chapter', models.IntegerField()),
                ('chapters_complete', models.IntegerField()),
                ('corresponding_cources', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.courses')),
            ],
        ),
    ]
