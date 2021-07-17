# Generated by Django 3.2.4 on 2021-07-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0007_auto_20210716_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate_resume',
            name='coverletter_link',
            field=models.FileField(blank=True, upload_to='cover_letter/<django.db.models.fields.related.ForeignKey>'),
        ),
        migrations.AlterField(
            model_name='candidate_resume',
            name='resume_link',
            field=models.FileField(blank=True, upload_to='resume/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]