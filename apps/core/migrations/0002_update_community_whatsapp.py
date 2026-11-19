from django.db import migrations, models

OLD_NUMBER = "+573160592569"
NEW_NUMBER = "+573160592569"


def forwards(apps, schema_editor):
    SiteConfiguration = apps.get_model("core", "SiteConfiguration")
    SiteConfiguration.objects.filter(community_whatsapp=OLD_NUMBER).update(
        community_whatsapp=NEW_NUMBER
    )


def backwards(apps, schema_editor):
    SiteConfiguration = apps.get_model("core", "SiteConfiguration")
    SiteConfiguration.objects.filter(community_whatsapp=NEW_NUMBER).update(
        community_whatsapp=OLD_NUMBER
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="siteconfiguration",
            name="community_whatsapp",
            field=models.CharField(
                default=NEW_NUMBER,
                max_length=20,
                verbose_name="WhatsApp de la comunidad",
            ),
        ),
        migrations.RunPython(forwards, backwards),
    ]
