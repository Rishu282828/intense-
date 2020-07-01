# Generated by Django 3.0.6 on 2020-06-24 07:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_apply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_Type', models.CharField(choices=[('PAS', 'PlacementAgency'), ('FLS', 'Freelancer'), ('NGO', 'Ngo'), ('TIS', 'TrainingInstitute'), ('CCS', 'CyberCafe'), ('CLG', 'College')], default='PLACEMENT_AGENCY', max_length=3)),
                ('organisation_Name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
