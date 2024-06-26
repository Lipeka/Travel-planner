

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Checking Date')),
                ('visit', models.CharField(default='Visited On', max_length=100)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.travel')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
