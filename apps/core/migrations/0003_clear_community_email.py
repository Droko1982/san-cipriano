from django.db import migrations, models


def clear_community_email(apps, schema_editor):
    """El correo de la comunidad ya no se publica: se vacia el valor guardado.

    El correo que recibe las consultas se configura en la variable de entorno
    COMMUNITY_EMAIL (privada) y no se guarda en la base de datos.
    """
    SiteConfiguration = apps.get_model("core", "SiteConfiguration")
    SiteConfiguration.objects.exclude(community_email="").update(community_email="")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_update_community_whatsapp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="siteconfiguration",
            name="community_email",
            field=models.EmailField(
                blank=True,
                default="",
                max_length=254,
                verbose_name="correo de la comunidad",
            ),
        ),
        migrations.RunPython(clear_community_email, migrations.RunPython.noop),
    ]
