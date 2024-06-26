

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0010_alter_travel_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='Checklist',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='status',
            new_name='checklists',
        ),
    ]
