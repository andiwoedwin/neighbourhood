# Generated by Django 2.2.6 on 2019-10-30 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
