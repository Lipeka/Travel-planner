
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_status_alter_checking_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='status',
            field=models.ManyToManyField(to='main_app.status'),
        ),
    ]
