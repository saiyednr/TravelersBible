# Generated by Django 4.1 on 2023-03-30 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0043_rename_file_path_eng_audio_file_path_english_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monument',
            old_name='info_hindi',
            new_name='info_Hindi',
        ),
    ]
